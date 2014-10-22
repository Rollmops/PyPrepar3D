#!/usr/bin/env python

import sys
import re
import os
import linecache

def parse_structs(content, output):
    
    in_struct = False
    current_struct_name = ''
    
    output.append('\n//----------------------------------------------------------------------------\n')
    output.append('//        Struct definitions\n')
    output.append('//----------------------------------------------------------------------------\n')

    
    for line in content:
        matches = re.match(r'^struct\s+(\w+)\s*(//.*)?$', line)
        if matches:
            current_struct_name = matches.group(1)
            if matches.group(2):
                output.append('\t%s\n' % matches.group(2))
            output.append('\tboost::python::class_<%s>(\"%s\")' % (current_struct_name, current_struct_name))
            in_struct = True

        matches = re.match(r'^struct\s+(\w+)\s*:\s*public\s+(\w+)\s*(//.*)?$', line)
        if matches:
            current_struct_name = matches.group(1)
            if matches.group(3):
                output.append('\t%s\n' % matches.group(3))
            output.append('\tboost::python::class_<%s, bases<%s> >(\"%s\")' % (current_struct_name, matches.group(2), current_struct_name))
            in_struct = True

        
        if in_struct:
            
            matches = re.match(r'^\s+static\s+const\s+\w+\s+(\w+).*;.*', line)
            if matches:
                output.append('\n\t\t.def_readonly(\"%s\", %s::%s)' % (matches.group(1), current_struct_name, matches.group(1)))
                continue
            
            matches = re.match(r'^\s+(\w+)\s+(\w+)(?:\[(.+)\])?;\s*(//.*)?', line)
            if matches:
                if matches.group(3):
                    if matches.group(1) == 'char':
                        _l = '\tto_python_converter<char [%s], prepar3d::converter::FROM_CHAR_ARRAY<%s> >();\n' % (matches.group(3), matches.group(3))
                        if _l not in output:
                            output.insert(0, _l)
                    else:
                        _l = '\tto_python_converter<%s [%s], prepar3d::converter::FROM_TYPE_ARRAY<%s, %s> >();\n' % (matches.group(1), matches.group(3), matches.group(1), matches.group(3))
                        if _l not in output:
                            output.insert(0, _l)
                if matches.group(4):
                    output.append('\n\t\t%s' % matches.group(4))
                output.append('\n\t\t.add_property(\"%s\", &%s::%s)' % (matches.group(2), current_struct_name, matches.group(2)))
                
            matches = re.match(r'^};$', line)
            if matches:
                in_struct = False
                output.append(';\n\n')          
        
    
def parse_enums(content, output):
    
    in_enum = False
    
    output.append('\n//----------------------------------------------------------------------------\n')
    output.append('//        Enum definitions\n')
    output.append('//----------------------------------------------------------------------------\n')
    
    for line in content:
        matches = re.match(r'^enum\s+(\w+)\s*{\s*(//.*)?$', line)
        if matches:
            if matches.group(2):
                output.append('\t%s\n' % matches.group(2))
            output.append('\tboost::python::enum_<%s>(\"%s\")' % (matches.group(1), matches.group(1)))
            in_enum = True
            
        if in_enum:
            matches = re.match(r'^\s*(\w+),.*', line)
            if matches:
                output.append('\n\t\t.value(\"%s\", %s)' % (matches.group(1), matches.group(1)))
            
            matches = re.match(r'^};$', line)
            if matches:
                in_enum = False
                output.append(';\n\n')          
            
def parse_constants(content, output):

    output.append('\n//----------------------------------------------------------------------------\n')
    output.append('//        Constants\n')
    output.append('//----------------------------------------------------------------------------\n\n')
    
    for line in content:
        matches = re.match(r'^\s*static\s+const\s+\w+\s+(\w+).*', line)
        if matches:
            output.append('\tscope().attr(\"%s\") = %s;\n' % ( matches.group(1), matches.group(1)))
            
            
if __name__ == '__main__':
    content = []
    output = []
    with open(sys.argv[1], 'r') as header_file:
        content = header_file.read().splitlines()

    parse_constants(content, output)
    parse_enums(content, output)        
    parse_structs(content, output)

    
    with open(os.path.join(os.getcwd(), 'parsed_file.txt'), 'w+') as output_file:
        [output_file.write(line) for line in output]
    
        
    

