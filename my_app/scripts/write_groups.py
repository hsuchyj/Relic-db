#to write group tags to modules.xml file
import xml.etree.ElementTree as ET
import ast, os

def create_exam_group_tags(question_groups):
    for items in question_groups.items():
        group_id_list = []
        for item in items[1]:
            group_string = '{'+'"type":"group","id":{}'.format(item)+'}'
            group_dict = ast.literal_eval(group_string)
            group_id_list.append(group_dict)
        
        #<availability>{"op":"|","c":[{"type":"group","id":5},{"type":"group","id":6}],"show":false}</availability>
        #my_tag = ("Question " + str(items[0]) + ': ' + '<availability>{"op":"|",' + '"c":{}'.format(str(group_id_list).replace("'", '"')) + ',"show":false}</availability>')
        my_tag_body = '{"op":"|",' + '"c":{}'.format(str(group_id_list).replace("'", '"')) + ',"show":false}'
        
        module_xml_file = "vpl/activities/vpl_" + str(items[0]) + "/module.xml"
        
        et = ET.parse(module_xml_file)
        
        # Append new tag: <a x='1' y='abc'>body text</a>
        root = et.getroot()
        availability = root.find('availability')
        availability.text = my_tag_body

        # Write back to file
        #et.write('file.xml')
        et.write(module_xml_file)    
        
        #print(my_tag_body)
        
def staff_tags(path, staff):
    
        sub_dirs = os.listdir(path)
        group_id_list = []
        
        group_string = '{'+'"type":"group","id":{}'.format(staff)+'}'
        group_dict = ast.literal_eval(group_string)
        group_id_list.append(group_dict)        
        
        for sub_dir in sub_dirs:          
            #<availability>{"op":"|","c":[{"type":"group","id":5},{"type":"group","id":6}],"show":false}</availability>
            #my_tag = ("Question " + str(items[0]) + ': ' + '<availability>{"op":"|",' + '"c":{}'.format(str(group_id_list).replace("'", '"')) + ',"show":false}</availability>')
            my_tag_body = '{"op":"|",' + '"c":{}'.format(str(group_id_list).replace("'", '"')) + ',"show":false}'
            
            module_xml_file = "vpl/activities/" + str(sub_dir) + "/module.xml"
            
            et = ET.parse(module_xml_file)
            
            # Append new tag: <a x='1' y='abc'>body text</a>
            root = et.getroot()
            availability = root.find('availability')
            availability.text = my_tag_body
    
            # Write back to file
            #et.write('file.xml')
            et.write(module_xml_file)