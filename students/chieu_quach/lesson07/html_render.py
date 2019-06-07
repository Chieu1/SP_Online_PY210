#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

import textwrap
textwrap.indent

indent           = 4
head_indent      = indent
head_indent_txt  = head_indent * 2
p_indent_txt     = head_indent_txt + 4
indent_txt       = p_indent_txt + 4

def indentation(text, number, currind=' '):
   padding = number * currind
   return ''.join(padding + line for line in text.splitlines(True))

# This is the framework for the base class
class Element(object):

    tag = "html"
    tagtype = ""
    def __init__(self, content=None, **Kwargs):
        global stylename_p
        global stylename_ul
        global stylename_li
        global stylename_meta
        for z in Kwargs:
        
         #   print ("z ", z)   
         #   print ("self.tag init ", self.tag)
         #   print ("content ", content)    
            if z == "style" and self.tag == "p":
                stylename_p = """<p style="text-align: center; font-style: oblique;">"""
                content = stylename_p + "\n" + str(content)
                self.tag = "pz"
            elif z == "id" and self.tag == "ul":
                stylename_ul = """<ul id="TheList" style="line-height:200%">"""
                content = stylename_ul
         #       print(content)
            elif z == "style" and self.tag == "li":
                stylename_li = """<li style="color: red">"""
                content = stylename_li + "\n" + str(content)
                self.tag = "liu"
            elif z == "charset" and self.tag == "meta":
                stylename_meta = """<meta charset="UTF-8" />"""
                content = stylename_meta
                
                      
        #  print ("content ", [content])   
        if content is not None:
           self.contents = [content]
           # This is where messages get printed

        if self.contents == ['DOCTYPE']:
            outprtz = """!DOCTYPE html"""
          #  self.tag = outprtz + "\n"
            self.tag = outprtz
            
          #  self.tag = "htmlz"
          #  print("self.content z", self.contents)
          #  print ("tag ",self.tag)
            
        if self.contents == ['i']:
           # make self.contents to "" to suppress printing extra line
           self.contents = ""
           pass
        else:
          # print("content is::", self.contents)
           pass
       
     #   print("self contents v ", self.contents)
       
    def append(self, new_content):
       # print ("self ", self)
       # print ("new_content", new_content)
        
        self.contents.append(new_content)
        pass

  #  def render(self, out_file, curr_ind=""):
   # def render(self, out_file, curr_ind='no'):
    def render(self, out_file, curr_ind=None):
     #   print ("self ", self)
     #   print ("curr_ind ", curr_ind)

        
        if curr_ind is None:
             
          #  
          # prints html with no indentation
          #
          #  print ("self.tag ", self.tag)
            
         #   print("curr ind is no")
            if self.tag == "p":
          # if self.tag == "p" or self.tag == "li":
                out_file.write("<{}>\n".format(self.tag))
            elif self.tag == "!DOCTYPE html":
                out_file.write("<{}>\n".format(self.tag))
                self.tag = "html"
                out_file.write("<{}>".format(self.tag))
        
            # bypass printing header tag if tag is equal to this name
            elif (self.tag == "pz" or self.tag == "hr" or 
                self.tag == "ul" or self.tag == "liu" or self.tag == "meta"):           
                pass
        
            else:
           # out_file.write("<{}>\n".format(self.tag))
                out_file.write("<{}>".format(self.tag))
            for content in self.contents:
            #    print("content u", content)
                try:                
                    content.render(out_file)
                    
                except AttributeError:
                    if content == "DOCTYPE":
                        pass
                    else:
                        out_file.write(content)
                
                # if tag == title write output in one line including <title>
                    if self.tag != "title":
                        out_file.write("\n")
                    

             #   print ("self.tag ", self.tag)      
             # prints the output content message             
             #   print ("self.contents ", self.contents)
            if self.tag == "liu":
               self.tag = "li"
            if self.tag == "pz":
               self.tag = "p"
           
            if self.tag == "hr":           
               out_file.write("<{} />\n".format(self.tag))
            elif self.tag == "meta":
               pass
            else:
               out_file.write("</{}>\n".format(self.tag))

               
    
        else:
            #
            # prints indentation
         
       #     print ("indentation yes ")
            curr_ind = "yes"
            nameindent = "<{}>".format(self.tag)
             #   if self.tag == "pz":
             # if self.tag == "p" or self.tag == "li":
             #  out_file.write("<{}>\n".format(self.tag))
            
            if self.tag == "!DOCTYPE html":
               out_file.write("<{}>\n".format(self.tag))
               self.tag = "html"
               out_file.write("<{}>".format(self.tag))
        
            # bypass printing header tag if tag is equal to this name
            elif (self.tag == "pz" or self.tag == "hr" or 
               self.tag == "ul" or self.tag == "liu" or self.tag == "meta"):           
               pass
        
            elif self.tag == "head":
            #     nameindent = "<{}>".format(self.tag)
               out_file.write(indentation(nameindent, head_indent))
            elif self.tag == "title":
            #   nameindent = "<{}>".format(self.tag)
               out_file.write(indentation(nameindent, head_indent_txt))
            elif self.tag == "body":          
               out_file.write(indentation(nameindent, head_indent))
            elif self.tag == "li":
               out_file.write(indentation(nameindent, p_indent_txt))
           
            else:
            # out_file.write("<{}>\n".format(self.tag))
                out_file.write("<{}>".format(self.tag))
            for content in self.contents:
           #    print("content u", content)
                try:                
                    content.render(out_file)
                   
                except AttributeError:
                    if content == "DOCTYPE":
                        pass
                    elif self.tag == "meta":
                        out_file.write(indentation(content, head_indent_txt))
                    elif self.tag == "pz":
                        out_file.write(indentation(stylename_p, head_indent_txt))
                        out_file.write(indentation(content, p_indent_txt))
                    elif self.tag == "ul":
                        out_file.write(indentation(stylename_ul, head_indent_txt))
                    elif self.tag == "li":
                        out_file.write(indentation(content, indent_txt))
                    elif self.tag == "liu":
                        out_file.write(indentation(stylename_li, p_indent_txt))
                        out_file.write(indentation(content, indent_txt))
                    else:
                        out_file.write(content)
                
                    # if tag == title write output in one line including <title>
                    if self.tag != "title":
                        out_file.write("\n")
                    

           #   print ("self.tag ", self.tag)      
           # prints the output content message             
           #   print ("self.contents ", self.contents)
            if self.tag == "liu":
                self.tag = "li"
            if self.tag == "pz":
                self.tag = "p"

            nameformat = "</{}>\n".format(self.tag)
            if self.tag == "hr":
          
                out_file.write(indentation(nameformat, head_indent_txt))  
           # out_file.write("<{} />\n".format(self.tag))
           #   out_file.write(indentation(nameformat, head_indent_txt))
            elif self.tag == "meta":
                pass
            elif self.tag == "head":
         #   nameformat = "</{}>\n".format(self.tag)
                out_file.write(indentation(nameformat, head_indent))
            elif self.tag == "p":
        #    nameformat = "</{}>\n".format(self.tag)
                out_file.write(indentation(nameformat, head_indent_txt))
            elif self.tag == "li":
                out_file.write(indentation(nameformat, p_indent_txt))
            elif self.tag == "ul":
                out_file.write(indentation(nameformat, head_indent_txt))
            elif self.tag == "body":
                out_file.write(indentation(nameformat, head_indent))
            else:
            
                out_file.write("</{}>\n".format(self.tag))



            
#     #   out_file.write("just something as a place holder...")

class Meta(Element):
    tag = "meta"

class Html(Element):

    tag = "html"
  #  tag = "!DOCTYPE html"
          
    
class Body(Element):
    tag = "body"
    
class A(object):
    tag = "a"
    def __init__(self, link, content):
    #    print ("self ", self)
        if link is not None:
            hrefmsg = """<a href="http://google.com", link</a> """
            content = hrefmsg + "\n"
       #     print(content)
       #     print ("link ", link)

        if content is not None:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)
        pass


    def render(self, out_file):

      #  if self.tag == "a":
           
         #   outfile.write("<{}>\n".format(self.tag))
       #     print ("self tag ", self.tag)
        for content in self.contents:
           
            try:                
                content.render(out_file)
            except AttributeError:           
                out_file.write(content)

class Li(Element):
    tag = "li"
                
class Ul(Element):
    tag = "ul"    



class Head(Element):
    tag = "head"


    
class Hr(Element):
    tag = "hr"
    
class P(Element):
    tag = "p"

class PZ(Element):
    tag = "pz"
    
class OneLineTag(Element):
    
    def render(self, out_file):
        for content in self.contents:
            
            out_file.write("<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))

      
    def append(self, content):
        raise NotImplementedError
    
class H(OneLineTag):
    tag = "h"

    def __init__(self, link, content=None, **Kwargs):
        super().__init__(content, **Kwargs)   

        if link is not None:
            self.tag = self.tag + str(link)
       #     print("link H ", self.tag)
            

        if content is not None:
            self.contents = [content]
            

        def append(self, new_content):
            self.contents.append(new_content)
            pass

class SelfClosingTag(Element):
    
    tag = "meta"
 
        
    
class Title(Element):
    tag = "title"
    
        
