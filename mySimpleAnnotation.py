def mySimpleAnnotation(*cities: str, separator: str = ", ", end: str = ".\t")-> None:
    """_briefcase by i-antoniou_,
        Short Description  --->,  
        prints dynamically,
        it feed it and respond the name or names of city/ies you give., 

    Parameters:,
        *cities (str): A variable must be a number.,
         The * means that you can give many var of city names to be printed.,
        
        separator (str, optional): _a symbol just to separate the names you give_,
        Default is ", ", but you can give "|" or "_" or "-" or "#" etc
        
        end (str, optional): _a symbol just to end the line of variable_,
        Default is "\t", but you can give another symbol.
    """

    if not cities:
        print("Not cities provided.")
    else:
        print("Cities displayed: ", separator.join(cities), end)

def main() -> None:
        """_summary_
        demo various str 
        """
        mySimpleAnnotation("Athens", "Paris", "London")

if __name__ == "__main__":
        main()

    