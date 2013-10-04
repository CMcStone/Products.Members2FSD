from zope.interface import Interface

class IMemberConverter(Interface):
    """ A utility to convert members
    """

    def convert(member):
        """ Take a member object and convert it to the destination
            member type.
        """
