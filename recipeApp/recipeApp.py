
from io import BytesIO
from PIL import Image, ImageTk
from playsound import playsound
from py_edamam import PyEdamam
import requests
import tkinter as tk
import webbrowser


BUTTON_CLICK_SOUND = "../clicks.m4a"
WINDOW_TITLE = "Recipe App"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300

class RecipeApp(object):

    def __init__(self, recipe_app_id, recipe_app_key):

        
        self.recipe_app_id = recipe_app_id
        self.recipe_app_key = recipe_app_key
        self.window = tk.Tk()
       
        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        self.search_label = tk.Label(self.window, text = "Search Recipe", bg = "#ea86b6")
        self.search_label.grid(column = 0, row = 0, padx=5)

        self.search_entry = tk.Entry(master = self.window, width = 40)
        self.search_entry.grid(column = 1, row = 0, padx=5, pady = 10)

        self.search_button = tk.Button(self.window, text = "search", highlightbackground = "#ea86b6",
            command = self.__run_search_query)
        self.search_button.grid(column = 2, row = 0, padx = 5)

       
    def __run_search_query(self):

        playsound(BUTTON_CLICK_SOUND)
        query = self.search_entry.get()
        recipe = self.__get_recipe(query)

        if recipe:
            recipe_image = recipe.image
            recipe_url = recipe.url
        
        else:
            # Recipe not found
            recipe_image = "https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg"
            recipe_url = ""

        self.__show_image(recipe_image)
        self.__get_ingredients(recipe)

        def __open_link():
            playsound(BUTTON_CLICK_SOUND)
            webbrowser.open(recipe_url)

        self.recipe_button = tk.Button(self.window, text = "recipe link", highlightbackground = "#ea86b6",
            command = __open_link)
        self.recipe_button.grid(column = 1, row = 7, pady = 10)


    def __get_recipe(self, query):
        edamam_object = PyEdamam(recipes_appid=self.recipe_app_id, recipes_appkey=self.recipe_app_key)
        query_result = edamam_object.search_recipe(query)
        
        # Get first recipe in list
        for recipe in query_result:
            return recipe
    
    def __show_image(self, image_url):
        response = requests.get(image_url)
        
        img = Image.open(BytesIO(response.content))
        img = img.resize((RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT))
        image = ImageTk.PhotoImage(img)
        
        holder = tk.Label(self.window, image = image)
        holder.photo = image
        holder.grid(column=1, row=6, pady=10)
    

    def __get_ingredients(self, recipe):
        ingredients = tk.Text(master = self.window, height = 15, width = 50, bg = "#ffdada")
        ingredients.grid(column=1,row=4, pady = 10)
        ingredients.delete("1.0", tk.END)  

        if recipe == None :
            ingredients.insert(tk.END, "No Recipe found for search criteria")
            return

        ingredients.insert(tk.END, "\n" + recipe.label + "\n")
        for ingredient in recipe.ingredient_names:
            ingredients.insert(tk.END, "\n- " + ingredient)

    def run_app(self):
        self.window.mainloop()
        return
      

# Create App and run the app
if __name__ == "__main__":
    #API Keys
    APP_ID = "" #Put your app id for edamam api
    APP_KEY = "" #Put your app key for edamam api

    recipe_app = RecipeApp(APP_ID, APP_KEY)
    recipe_app.run_app()
  
