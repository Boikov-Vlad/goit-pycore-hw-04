def show_phone(args, contacts):
    if len(args) < 2:
        return "Wrong contact data format. Please use 'change [name] [phone number]' format"
    
    name = args[0]
    
    if name not in contacts:
        return f"Error: Contat {name} is not found"
    
    return contacts[name]