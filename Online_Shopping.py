from easygui import *
import sys

while 1:
    msgbox("Bonjour")

    msg ="Which site do you prefer?"
    title = "Online Shopping"
    choices = ["Amazon", "Flipkart", "Snapdeal", "Myntra"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    
    if choice=="Amazon":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          msg="Dell-40,00rs, Lenovo-60.000rs,Apple-1cr Rs"

      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          msg="F21-400rs,UCB-60.000rs,Zara-1cr Rs"
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
    elif choice=="Flipkart":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
    elif choice=="Snapdeal":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
    elif choice=="Myntra":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
else:
	sys.exit(0)
