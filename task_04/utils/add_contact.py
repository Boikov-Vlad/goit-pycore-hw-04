def add_contact(args, contacts):
    if len(args) < 2:
        return "Wrong contact data format. Please use 'change [name] [phone number]' format"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."