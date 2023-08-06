import requests
import hashlib
import sys


class InvalidQueryException(Exception):
    pass


def get_breach_count(hash_to_check, hashes_list):
    hashes_list = (pw_hash.split(":") for pw_hash in hashes_list)
    breached_count = 0
    for current_hash, count in hashes_list:
        if current_hash == hash_to_check:
            breached_count = count
            break
    return breached_count


def call_api(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    response = requests.get(url)
    if response.status_code != 200:
        raise InvalidQueryException(f"Opps!. Seems like the query_character, {query_char} is invalid")
    return response


def get_hashed_password(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


def get_breached_count(password):
    hashed_pw = get_hashed_password(password)
    query_char = hashed_pw[:5]
    tail = hashed_pw[5:]

    response = call_api(query_char)
    hashes_list = response.text.splitlines()

    breached_count = get_breach_count(tail, hashes_list)
    return int(breached_count)


def main(passwords_to_check):
    try:
        for password in passwords_to_check:
            breached_count = get_breached_count(password)
            if breached_count > 0:
                print(
                    f"{password} was found breached {breached_count} times. You should consider changing your password.")
            else:
                print(f"Congratulations! Your password {password} was not breached in any data leaks")
    except InvalidQueryException as e:
        print(e.args[0])

    print("\nCheck Completed.")


if __name__ == "__main__":
    passwords = sys.argv[1:]
    print("Password is being Checked. Please wait.\n")
    main(passwords)

# Improvement: Instead of command prompt, try getting password from a text file
