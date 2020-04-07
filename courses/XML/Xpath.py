from lxml import etree

xml_doc = """
<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="Lesson04_Schema.xsd"><persons><person person_id="f1"><person_name>张三</person_name><gender>male</gender><age>48</age><address><address_info>武昌区珞珈山</address_info><post_code>430072</post_code></address><cellphone>13800000001</cellphone><company_affiliated company_id="c1">武汉大学</company_affiliated></person><person person_id="f2"><person_name>李四</person_name><gender>female</gender><age>20</age><address><address_info>武昌区珞珈山</address_info><post_code>430072</post_code></address><cellphone>13800000002</cellphone><company_affiliated company_id="c1">武汉大学</company_affiliated></person><person person_id="f3"><person_name>王五</person_name><gender>male</gender><age>28</age><address><address_info>武昌区街道口</address_info><post_code>430079</post_code></address><cellphone>13800000003</cellphone><company_affiliated company_id="c2">小米武汉</company_affiliated></person></persons><companies><company company_id="c1"><company_name company_type="大学">武汉大学</company_name><code/><address><address_info>武昌区珞珈山</address_info><post_code>430072</post_code></address><phone>027-68750001</phone><employees><employee person_id="f1">张三</employee><employee person_id="f2">李四</employee></employees></company><company company_id="c2"><company_name company_type="IT企业">小米武汉</company_name><code/><address><address_info>武昌区街道口</address_info><post_code>430079</post_code></address><phone>027-68750001</phone><employees><employee person_id="f3">王五</employee></employees></company></companies></root>
"""

mytree = etree.XML(xml_doc)

print(mytree.xpath("//address"))
print(mytree.xpath("//persons/descendant::*[@company_id='c1']"))
print(mytree.xpath("//persons/descendant::*[age>25]/age"))
print(mytree.xpath("//persons/person[2]/following::*"))
print(mytree.xpath("//persons/person[2]/following-sibling::*"))

print(mytree.xpath("/root/persons/person[1]/address/descendant-or-self::*"))
print(mytree.xpath("/*/*/person[2]/address/following::*"))
print(mytree.xpath("//person[2]/person_name | //company[1]/company_name"))
