def show_all(args, contacts):
    if not contacts:
        return "No saved contacts available"
    
    all_contacts = "Contacts:\n"
    
    for name, phone in contacts.items():
        all_contacts += f"{name} : {phone}\n"
        
    return all_contacts
    