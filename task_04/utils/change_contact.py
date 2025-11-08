def change_contact(args, contacts):
    if len(args) < 2:
        return "Wrong contact data format. Please use 'change [name] [phone number]' format"
    
    name, phone = args

    if name not in contacts:
        return f"Error: Contat {name} is not found"
    
    contacts[name] = phone
    return "Contact updated."
    
    