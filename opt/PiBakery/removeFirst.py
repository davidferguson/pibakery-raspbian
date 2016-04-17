# Removes the first boot blockly xml from /boot/PiBakery/blocks.xml 

from xml.dom import minidom

xmldoc = minidom.parse('/boot/PiBakery/blocks.xml')
root = xmldoc.documentElement

blocks = xmldoc.getElementsByTagName('block')
for block in blocks:
	if block.hasAttribute('type'):
		if block.getAttribute('type') == 'onfirstboot':
			root.removeChild(block)

blockFile = open('/boot/PiBakery/blocks.xml','wb')
root.writexml(blockFile)
blockFile.close()