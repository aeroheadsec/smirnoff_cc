##
## Cross compiler for you singular golang scripts.
##
## Windows, Mac, Linux and FreeBSD cross compilation.
##

import os
import colorama
import subprocess

## You can add much architectures as you want, to see what archs you can compile for, run:
## go tool dist list
ALL_PLATFORMS = ['darwin/amd64', 'linux/amd64', 'linux/386', 'linux/arm', 'freebsd/amd64', 'freebsd/386', 'windows/amd64', 'windows/386', 'linux/arm64', 'linux/mips', 'linux/mips64', 'linux/mips64le', 'linux/mipsle', 'linux/ppc64']
BINARIES_DIR = 'BINARIES'

SMIRNOFF = r'''
                   _                  ________
   _________ ___  (_)________  ____  / __/ __/
  / ___/ __ `__ \/ / ___/ __ \/ __ \/ /_/ /_  
 (__  ) / / / / / / /  / / / / /_/ / __/ __/  
/____/_/ /_/ /_/_/_/  /_/ /_/\____/_/ /_/     
                                                                     
Compile your Golang scrips for Windows, Mac, Linux and FreeBSD operating systems.

https://github.com/aeroheadsec/smirnoff_cc

'''

def compile_for_platform(platform, source_file):
    os.makedirs(BINARIES_DIR, exist_ok=True)
    os_name, arch = platform.split('/')
    output_ext = '.exe' if os_name == 'windows' else '.bin'
    output_filename = f'{os_name}_{arch}{output_ext}'
    if os_name == "windows":
        cmd = ['env', f'GOARCH={arch}', f'GOOS={os_name}', 'go', 'build', '-o', os.path.join(BINARIES_DIR, output_filename)]
    else:
        cmd = ['env', f'GOARCH={arch}', f'GOOS={os_name}', 'go', 'build', '-o', os.path.join(BINARIES_DIR, output_filename)]
    cmd.append(source_file)

    subprocess.run(cmd, check=True)
    
    # Make the compiled binary executable
    if os_name != 'windows':
        binary_path = os.path.join(BINARIES_DIR, output_filename)
        os.chmod(binary_path, 0o755)  # Set executable permissions

def main():
    print(colorama.Fore.RED + SMIRNOFF)
    
    source_file = input("Enter the filename of the Go source script: " + colorama.Fore.WHITE)
    
    for platform in ALL_PLATFORMS:
        print(f"{colorama.Fore.YELLOW}[?] Compiling for {platform}...")
        compile_for_platform(platform, source_file)
        print(f"{colorama.Fore.GREEN}Compilation for {platform} complete.")

    print(f"\n\n{colorama.Fore.GREEN}Cross compilation has been complete! See {BINARIES_DIR}/ to view compiled executables!{colorama.Fore.WHITE}\n\n")

if __name__ == '__main__':
    main()
