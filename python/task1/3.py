import os
path = os.getenv('PATH')
print(f'PATH: {path}')
print("\nAll environment variables:")
for key, value in os.environ.items():
    print(f'{key}: {value}')
