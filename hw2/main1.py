from fastapi import FastAPI

app = FastAPI()

@app.get("/calculator")
def main(operation:str, num1:float, num2:float):
    if operation == "+":
        return {"result":num1 + num2}
    if operation == "-":
        return {"result":num1 - num2}
    else:
        return {"message":"invalid operation"}