#!/usr/bin/env python
import sys, re

class BlockType:
    start_cre = re.compile(r'^typedef [a-z]+ {.*')
    end_cre = re.compile(r'^}[ ]*(SaHpi.*);')
    member_cre = re.compile(r'^[ ]*SaHpi[A-Za-z0-9]+[ ]+[A-Za-z0-9]+[\[A-Z_\]]*[ ]*;.*')
        
    def __init__(self, name, block):
        self.datatype = 'unknown'
        self.name = name
        self.block = block
        self.members = []

    def __str__(self):
        str = self.name + '\n'
        for m in self.members:
            name = m.name
            if m.datatype == 'array':
                name += '[' + m.lenstr + ']'
            str += '    %s %s (%s)\n' % (m.typename, name, m.datatype)
        return str
    
    def parse(self, blocks):
        for b in self.block:
            if self.member_cre.match(b):
                self.members.append(Member(b, blocks))

class Struct(BlockType):
    start_cre = re.compile(r'^typedef struct {.*')
        
    def __init__(self, name, block):
        BlockType.__init__(self, name, block)
        self.datatype = 'struct'

class Union(BlockType):
    start_cre = re.compile(r'^typedef union {.*')
        
    def __init__(self, name, block):
        BlockType.__init__(self, name, block)
        self.datatype = 'union'

class Member:
    member_cre = re.compile(r'^[ ]*(SaHpi[A-Za-z0-9]+)[ ]+([A-Za-z0-9]+)[ ]*;.*')
    array_cre = re.compile(r'^[ ]*(SaHpi[A-Za-z0-9]+)[ ]+([A-Za-z0-9]+)\[([A-Z_]+)\][ ]*;.*')
    
    def __init__(self, bline, blocks):
        match = self.member_cre.match(bline)
        if match:
            try:
                self.datatype = blocks[match.groups()[0]].datatype
            except KeyError:
                self.datatype = 'native'
        else:
            match = self.array_cre.match(bline)
            if match:
                self.datatype = 'array'
                self.lenstr = match.groups()[2]
            else:
                print 'ERROR: Could not match member line: %s' % bline
                sys.exit(1)
            
        self.typename = match.groups()[0]
        self.name = match.groups()[1]

class HeaderParser:
    def __init__(self, filename, types):
        self.filename = filename
        self.types = types
                
    def parse(self):
        blocks = {}
        header_file = open(self.filename, 'r')
        line = header_file.readline()
        while line:
            for T in self.types:
                if T.start_cre.match(line):
                    block = []
                    bline = header_file.readline()
                    match = T.end_cre.match(bline)
                    while not match:
                        block.append(bline[:-1])
                        bline = header_file.readline()
                        match = T.end_cre.match(bline)
                    blockname = match.groups()[0]
                    blocks[blockname] = T(blockname, block)
            line = header_file.readline()
        
        for block in blocks.values():
            block.parse(blocks)
        
        return blocks

if __name__ == '__main__':
    blocks = HeaderParser(sys.argv[1], [Struct, Union]).parse()
    for block in blocks.values():
        extends = '%%extend %s {\n' % (block.name)
        extends += '\t%s(' % (block.name)
        args = []
        for m in block.members:
            if m.datatype == 'array':
                args.append('%s %s[%s] = NULL' % (m.typename, m.name, m.lenstr))
            elif m.datatype in ['struct', 'union']:                
                args.append('%s *%s = NULL' % (m.typename, m.name))
            else:
                args.append('%s %s = 0' % (m.typename, m.name))
        extends += ', '.join(args)
        extends += ') {\n'
        extends += '\t\t%s *o;\n' % (block.name)
        extends += '\t\to = (%s *)malloc(sizeof(%s));\n' % (block.name, block.name)
        extends += '\t\tmemset(o, 0, sizeof(%s));\n' % block.name
        args = []
        for m in block.members:
            # Need and exception here for SaHpiGuidT. It is obscurely defined.
            if m.typename == 'SaHpiGuidT':
                args.append('\t\tif (%s) memcpy(o->%s, %s, sizeof(%s));' % (m.name, m.name, m.name, m.typename))
            elif m.datatype == 'array':
                args.append('\t\tif (%s) memcpy(o->%s, %s, sizeof(%s)*%s);' % (m.name, m.name, m.name, m.typename, m.lenstr))
            elif m.datatype in ['struct', 'union']:
                args.append('\t\tif (%s) o->%s = *%s;' % (m.name, m.name, m.name))
            else:
                args.append('\t\to->%s = %s;' % (m.name, m.name))
        extends += '\n'.join(args)
        extends += '\n\t\treturn o;\n'
        extends += '\t}\n};\n'
        print extends
        #print block
