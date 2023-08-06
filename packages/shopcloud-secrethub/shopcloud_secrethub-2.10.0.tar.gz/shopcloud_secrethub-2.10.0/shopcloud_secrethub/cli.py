import json
import os
import re
import pwd
import getpass

from .app import App, ConfigFile
from . import exceptions


def get_username():
    try:
        return pwd.getpwuid( os.getuid())[0]
    except Exception as e:
        return None


def main(args):
    path = os.path.expanduser('~/.secrethub')
    username = get_username()
    command = args.which

    if command == 'auth':
        token = getpass.getpass('Token:')
        ConfigFile.generate(path, token)
    elif command == 'token-refresh':
        app = App(path)
        new_token = app.token_refresh()    
        ConfigFile.generate(path, new_token)
    elif command == 'read':
        app = App(path)
        try:
            secrets = app.read(args.name, user_app=username)
        except exceptions.APIAuthError as e:
            print('Authentication Error - Token invalid')
            exit(1)
        except exceptions.APIError as e:
            print('API Error')
            exit(1)
        except Exception as e:
            print(f'Error {e}')
            exit(1)
        if len(secrets) == 0:
            raise Exception('can not access secret `{}`'.format(args.name))
        if args.output is None:
            for secret in secrets:
                value = secret.get('value').encode('unicode_escape').decode('utf-8')
                print(f"{secret.get('name')}={value}")
        elif args.output == 'raw':
            for secret in secrets:
                value = secret.get('value').encode('unicode_escape').decode('utf-8')
                print(value.replace('\\n', "\n"))
        elif args.output == 'json':
            for secret in secrets:
                print(json.dumps(secret))
    elif command == 'write':
        app = App(path)

        if args.in_file is not None:
            with open(args.in_file) as f: 
                s = f.read()
                try:
                    app.write(args.name, s, user_app=username)
                except exceptions.APIAuthError as e:
                    print('Authentication Error - Token invalid')
                    exit(1)
                except exceptions.APIError as e:
                    print('API Error')
                    exit(1)
                except Exception as e:
                    print(f'Error {e}')
                    exit(1)
        else:
            if args.value is None:
                raise Exception("value must set")
            try:
                app.write(args.name, args.value, user_app=username)
            except exceptions.APIAuthError as e:
                print('Authentication Error - Token invalid')
                exit(1)
            except exceptions.APIError as e:
                print('API Error')
                exit(1)
            except Exception as e:
                print(f'Error {e}')
                exit(1)
    elif command == 'inject' or command == 'printenv':
        app = App(path)

        with open(args.i) as f:
            template = f.read()

        def extract(x):
            name = x.replace("{{", '').replace('}}', '').strip()
            try:
                secrets = app.read(name, user_app=username)
            except exceptions.APIAuthError as e:
                print('Authentication Error - Token invalid')
                exit(1)
            except exceptions.APIError as e:
                print('API Error')
                exit(1)
            except Exception as e:
                print(f'Error {e}')
                exit(1)
            if len(secrets) == 0:
                raise AttributeError("Secret not found {}".format(name))
            key_s = "/".join(name.split('/')[-1:]).upper().replace('/', '_').replace('-', '_')
            return (x, key_s, secrets[0].get('value'))

        variables = [extract(x) for x in re.findall('{{.*}}', template)]

        if command == 'printenv':
            for _, key, value in variables:
                value = value.replace('$', '\$')
                print(f"export {key}=\"{value}\"")
        else:
            for key, _, value in variables:
                template = template.replace(key, f"\"{value}\"")
            with open(args.o, 'w') as writer:
                writer.write(template)
