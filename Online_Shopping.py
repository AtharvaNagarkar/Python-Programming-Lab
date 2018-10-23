from easygui import *
import sys
sum=0
list=[]
while 1:
      msgbox("Welcome")
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
	   	 if choice=="Dell":
			msg="Select vendor and price"
			title="Dell"
			choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
			choice=choicebox(msg, title, choices)
		 elif choice=="Apple":
                        msg="Select vendor and price"
                        title="Apple"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
	       	 else:
                        msg="Select vendor and price"
                        title="Lenovo"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Clothing":
        	  msg="What do you want to buy?"
        	  title="Shop clothing"
        	  choices=["Forever 21","UCB","Zara"]
        	  choice=choicebox(msg, title, choices)
		  if choice=="Forever 21":
			msg="Select vendor and price"
			title="Forever 21"
			choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
			choice=choicebox(msg, title, choices)
		  elif choice=="UCB":
                        msg="Select vendor and price"
                        title="UCB"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
		  else:
                        msg="Select vendor and price"
                        title="Zara"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Furniture":
         	  msg="What do you want to buy?"
         	  title="Shop furniture"
        	  choices=["Sofa","Bed","Table"]
        	  choice=choicebox(msg, title, choices)
		  if choice=="Sofa":
			msg="Select vendor and price"
			title="Sofa"
			choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
			choice=choicebox(msg, title, choices)
                  elif choice=="Bed":
                        msg="Select vendor and price"
                        title="Bed"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
		  else:
                        msg="Select vendor and price"
                        title="Table"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
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
                  if choice=="Dell":
                        msg="Select vendor and price"
                        title="Dell"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="Apple":
                        msg="Select vendor and price"
                        title="Apple"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Lenovo"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices) 
          elif choice=="Clothing":
        	  msg="What do you want to buy?"
        	  title="Shop clothing"
        	  choices=["Forever 21","UCB","Zara"]
        	  choice=choicebox(msg, title, choices)
                  if choice=="Forever 21":
                        msg="Select vendor and price"
                        title="Forever 21"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="UCB":
                        msg="Select vendor and price"
                        title="UCB"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Zara"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Furniture":
        	  msg="What do you want to buy?"
        	  title="Shop furniture"
        	  choices=["Sofa","Bed","Table"]
        	  choice=choicebox(msg, title, choices)
		  if choice=="Sofa":
                        msg="Select vendor and price"
                        title="Sofa"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="Bed":
                        msg="Select vendor and price"
                        title="Bed"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Table"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
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
                  if choice=="Dell":
                        msg="Select vendor and price"
                        title="Dell"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="Apple":
                        msg="Select vendor and price"
                        title="Apple"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Lenovo"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Clothing":
        	  msg="What do you want to buy?"
        	  title="Shop clothing"
        	  choices=["Forever 21","UCB","Zara"]
        	  choice=choicebox(msg, title, choices)
                  if choice=="Forever 21":
                        msg="Select vendor and price"
                        title="Forever 21"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="UCB":
                        msg="Select vendor and price"
                        title="UCB"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Zara"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Furniture":
        	  msg="What do you want to buy?"
        	  title="Shop furniture"
        	  choices=["Sofa","Bed","Table"]
        	  choice=choicebox(msg, title, choices)
		  if choice=="Sofa":
                        msg="Select vendor and price"
                        title="Sofa"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="Bed":
                        msg="Select vendor and price"
                        title="Bed"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Table"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
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
                 if choice=="Dell":
                        msg="Select vendor and price"
                        title="Dell"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                 elif choice=="Apple":
                        msg="Select vendor and price"
                        title="Apple"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
                 else:
                        msg="Select vendor and price"
                        title="Lenovo"
                        choices=["v1:Rs.30,000","v2:Rs.32,000","v3:Rs.35,000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Clothing":
        	  msg="What do you want to buy?"
        	  title="Shop clothing"
        	  choices=["Forever 21","UCB","Zara"]
        	  choice=choicebox(msg, title, choices)
                  if choice=="Forever 21":
                        msg="Select vendor and price"
                        title="Forever 21"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  elif choice=="UCB":
                        msg="Select vendor and price"
                        title="UCB"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
                  else:
                        msg="Select vendor and price"
                        title="Zara"
                        choices=["v1:Rs.2000","v2:Rs.2500","v3:Rs.3000"]
                        choice=choicebox(msg, title, choices)
          elif choice=="Furniture":
         	 msg="What do you want to buy?"
         	 title="Shop furniture"
         	 choices=["Sofa","Bed","Table"]
         	 choice=choicebox(msg, title, choices)
		 if choice=="Sofa":
                        msg="Select vendor and price"
                        title="Sofa"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                 elif choice=="Bed":
                        msg="Select vendor and price"
                        title="Bed"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
                 else:
                        msg="Select vendor and price"
                        title="Table"
                        choices=["v1:Rs.50,000","v2:Rs.55,000","v3:Rs.60,000"]
                        choice=choicebox(msg, title, choices)
      msg = "Do you want to continue ? "
      title = "Please Confirm"
      if ccbox(msg, title):     # show a Continue/Cancel dialog
                 pass  # user chose Continue
      else:
	 	 sys.exit(0)
