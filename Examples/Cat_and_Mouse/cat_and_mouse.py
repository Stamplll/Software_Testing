def cat_and_mouse(x: int, y: int, z: int) -> str:
    distA = abs(x - z)
    distB = abs(y - z)

    if distA < distB:
        return "Cat A"
    elif distA > distB:
        return "Cat B"
    else:
        return "Mouse C"
    
if __name__ == "__main__":
    input_str = input("Enter A B C: ")
    line = map(int, input_str.split())

    result = cat_and_mouse(*line)
    print(f"Result: {result}")