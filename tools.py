
# Each tool in a way of writing

tools = [

    {

    "type": "function",
        "function": {
        "name": "add",
    "description": "Add two numbers",
    "parameters":
        {
            "type" : "object",
            "properties":

        {
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"]

        }

    }

},

    {

    "type": "function",
        "function": {
        "name": "subtract",
    "description": "subtract b from a",
    "parameters":
        {
            "type" : "object",

            "properties":{
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"]

        }

    }

},


{

    "type": "function",
        "function": {
        "name": "multiply",
    "description": "multiply a and b",
    "parameters":
        {
            "type" : "object",

            "properties":{
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"]

        }

    }

},



{

    "type": "function",
        "function": {
        "name": "divide",
    "description": "divide a by b",
    "parameters":
        {
            "type" : "object",

            "properties":{
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"]

        }

    }

},




]