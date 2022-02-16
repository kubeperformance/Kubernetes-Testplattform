import os

kustomize_command = 'kustomize build github.com/xridge/kubestone/config/samples/fio/overlays/pvc'

# Gets current working directory
cwd = os.getcwd()

my_filename = 'kOut.txt'

def make_system_call(command):
    os.system(command)

def echo_something(to_echo):
    os.system('echo ' + to_echo)

def write_output_to_file(command, file_name):
    os.system(command + '>' + file_name)


os.system('echo \'Starting System Communication Module...\'')

#os.system('cd ' + cwd)
os.system('echo \'Working Directory: \'')

print(cwd)

write_output_to_file(kustomize_command, my_filename)

echo_something('Printing output of file...')
make_system_call('cat ' + my_filename)




