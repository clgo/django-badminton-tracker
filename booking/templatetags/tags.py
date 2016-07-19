from django import template

register = template.Library()

#   @register.tag
#   def active(parse, token):
#   	args = token.split_contents()
#   	template_tag = args[0]
#   	if len(args) < 2:
#   		raise template.TemplateSyntaxError, "%r tag requires at least one argument" % template_tag
#   	return NavSelectedNode(args[1:])		

@register.simple_tag
def active(request, pattern):
	import re
	if re.search(pattern, request.path):
		return 'active'
	return ''



#class NavSelectedNode(template.Node):
#	def __init__(self, patterns):
#		self.patterns = patterns
#
#	def render(self, context):
#		path = context['request'].path
#		for p in self.patterns:
#			pValue = template.Variable(p).resolve(context)
#			if path == pValue:
#				return "active" # change this if needed for other bootstrap version (compatible with 3.2)
#		retun ""