class Group(object):
	def __init__(self, _name):
		self.name = _name
		self.groups = []
		self.users = []

	def add_group(self, group):
		self.groups.append(group)

	def add_user(self, user):
		self.users.append(user)

	def get_groups(self):
		return self.groups

	def get_users(self):
		return self.users

	def get_name(self):
		return self.name

def is_user_in_group(user, group):
	"""
	Return True if user is in the group, False otherwise.

	Args:
		user(str): user name/id
		group(class:Group): group to check user membership against
	"""
	if user == "" or user is None:
		return "Set values for user"
	if group == "" or group is None:
		return "Set values for group"
	if not isinstance(group, Group):
		return "Invalid group input!"
	if user in group.get_users():  # User found
		return True
	else:
		if len(group.get_groups()) == 0:  # Keep searching
			return False
		else:
			for sub_group in group.get_groups():
				found = is_user_in_group(user, sub_group)
	return found
				
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test
print(is_user_in_group(user="parent_user", group=parent))
#False
print(is_user_in_group(user="child_user", group=parent))
#False
print(is_user_in_group(user="sub_child_user", group=parent))
# True

# Edge Case
print(is_user_in_group(user="other_group", group=parent))
# False
print(is_user_in_group(user="", group=parent))
# Set values for user and group
print(is_user_in_group(user="sub_child_user", group=sub_child_user))
# Invalid group input!