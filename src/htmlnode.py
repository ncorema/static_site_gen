class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html += f" {prop}={self.props[prop]}"
        return html
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, comp):
        return self.tag == comp.tag and self.value == comp.value and self.children == comp.children and self.props == comp.props
