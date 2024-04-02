import sqlite3

connection = sqlite3.connect('db/database.db')

with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('greetings', 'Hello~Hi~Greetings', 'Hello!'))
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('greetings', 'Hi, How is it going?~Hi, How is it going?~Hi, How is it going?~Hi, How is it going?~Hi, How is it going?~Hi, How is it going?~How are you doing?', 'Good~Fine~Okay~Great~Could be better.~Not so great.~Very well, thanks.') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('greetings', 'How are you doing?~How are you doing?~How do you do?~How do you do?', 'Good.~Fine, and you?~Im doing well.') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('greetings', 'Hi, nice to meet you.~It is a pleasure to meet you.~Top of the morning to you!', 'Thank you. You too.~Thank you. You too.') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('greetings', 'What s up?', 'Not much.~Not too much.~Not much, how about you?~Nothing much.~The skys up but I am fine thanks. What about you?') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('acc_greetings', 'What is accommodations like in Southampton~How are the living conditions in Southampton?~What kind of places can you stay in Southampton?~How is the quality and availability of accommodations in Southampton?~What are the options and prices for accommodations in Southampton?~How would you rate the accommodations in Southampton?',
                                                                              'Budget friendly~Southampton has a variety of hotels, B&Bs, guesthouses, and apartments to suit different budgets and preferences~Southampton offers varieties like hotels,guesthouses and apartments~Southampton has a variety of hotels, B&Bs, guesthouses, and apartments to suit different budgets and preferences~Southampton offers varieties like hotels,guesthouses and apartments') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('accomodation_inquiry', 'What are the advantages and disadvantages of living in private accommodations?~How do private accommodations compare to other types of housing?~What are the benefits and drawbacks of choosing private accommodations?~What are the positive and negative aspects of private accommodations?~How do private accommodations affect your living experience?', 
                                                                             'Advantages include more social life,  safety and security~ great value for money. Cons include limited choice, rowdy during the evening, lose some of the independence') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('sources', 'How to find trustworthy accommodation sources?~Reliable sites for hotels or rentals?~Where to search for quality accommodations?', 
                                                                             'Southampton City Council website,sites like Zoopla, Rightmove and SpareRoom or local newspapers~Southern Daily Echo and Property Advertiser~visit agent offices around the city~local newspapers') )
cur.execute("INSERT INTO intent (tag, pattern, response) VALUES (?, ?, ?)", ('bills', 'What are the different types of utilities that renters have to pay for?~How can renters categorize the utilities that they have to pay for?~What kinds of utilities are included in the renter\'s expenses?~Utilities for renters: what are the different types?~Tell me about bills', 
                                                                             'Utilities for renters include gas, electricity, water, internet, TV license, and council tax.~Renters pay for utilities such as gas, electricity, water, internet, TV license, and council tax.') )
connection.commit()
connection.close()