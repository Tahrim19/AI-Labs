# 1-
def store_city_data():
    file = open("city.txt", "a")
    while True:
        city_name = input("Enter city name (type 'exit' to finish): ")
        if city_name.lower() == 'exit':
            break
        population = input("Enter population: ")
        mayor = input("Enter mayor's name: ")
        file.write(f"{city_name},{population},{mayor}\n")
    print("Data stored.")
    file.close()

store_city_data()


# 2-
def students():
    file = open("student.txt", "a")
    file.write("Now we are AI students" + "\n")
    print("Message written.")
    file.close()

students()
