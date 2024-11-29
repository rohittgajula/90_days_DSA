
# with inbuilt functions
def unique_email_1(emails):
    unique_email = set()

    for e in emails:
        local, domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        unique_email.add((local, domain))
    return len(unique_email)

# with inbuilt function
def unique_email(emails):
    uniquemails = set()
    for e in emails:
        local, domain = e.split('@')
        temp = []
        for char in local:
            if char == ".":
                continue
            if char == "+":
                break
            temp.append(char)
        uniquemails.add("".join(temp)+'@'+domain)
    return len(uniquemails)

# withot inbuilt functions
def unique_email_without_inbuilt_functions(emails):
    unique_email = set()

    for e in emails:
        i = 0
        local = ""

        # Process the local part of the email
        while e[i] not in ["@", "+"]:
            if e[i] != ".":
                local += e[i]
            i += 1
        
        # Skip everything until '@' if there's a '+' character
        while e[i] != "@":
            i += 1

        # Get the domain part after '@'
        domain = e[i+1:]

        # Add the unique (local, domain) pair to the set
        unique_email.add((local, domain))
    return len(unique_email)



emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(unique_email_1(emails))
print(unique_email(emails))
print(unique_email_without_inbuilt_functions(emails))