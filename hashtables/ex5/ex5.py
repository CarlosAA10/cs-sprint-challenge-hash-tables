# Your code here

cache = {}

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = [] 

    for file in files:

        chopped = file.split("/")

        # return chopped[-1] returns last element in chopped list, our query if it exists

        cache[chopped[-1]] = file # creates dictoinary with last thing as key, and value as the whole pathj


    for query in queries:

        if query in cache:
            result.append(cache[query])


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
