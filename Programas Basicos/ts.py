def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

def run():
    #Para definir constantes en lugar de variables, utiliza mayúsculas
    print(find_max({10,3,55}))

#Entrypoint / punto de entrada
if __name__ == "__main__":
    run()