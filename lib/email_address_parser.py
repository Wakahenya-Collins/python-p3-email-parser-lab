# your code goes here!
import re

class EmailAddressParser:
    
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        strings = re.split(r',|\s', self.emails)
        
        parsed_emails = set()
        for string in strings:
            if self.email_regex.fullmatch(string):
                parsed_emails.add(string)

        return sorted(list(parsed_emails))

# Example usage
email_addresses = "john@doe.com, person@somewhere.org"
parser = EmailAddressParser(email_addresses)
parsed_emails = parser.parse()
print(parsed_emails)  # Output: ["john@doe.com", "person@somewhere.org"]


