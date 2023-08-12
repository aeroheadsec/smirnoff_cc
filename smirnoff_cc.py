##
## Cross compiler for you singular golang scripts.
##
## Windows, Mac, Linux and FreeBSD cross compilation.
##

import os
import colorama
import subprocess

ALL_PLATFORMS = ['darwin/amd64', 'linux/amd64', 'linux/386', 'linux/arm', 'freebsd/amd64', 'freebsd/386', 'windows/amd64', 'windows/386', 'linux/arm64']
BINARIES_DIR = 'BINARIES'

SMIRNOFF = r'''
                   _                  ________
   _________ ___  (_)________  ____  / __/ __/
  / ___/ __ `__ \/ / ___/ __ \/ __ \/ /_/ /_  
 (__  ) / / / / / / /  / / / / /_/ / __/ __/  
/____/_/ /_/ /_/_/_/  /_/ /_/\____/_/ /_/     
                                                                     
Compile your Golang scrips for Windows, Mac, Linux and FreeBSD operating systems.

https://github.com/dharmade/smirnoff_cc

'''

def compile_for_platform(platform, source_file):
    os.makedirs(BINARIES_DIR, exist_ok=True)

    os_name, arch = platform.split('/')
    output_ext = '.exe' if os_name == 'windows' else '.bin'
    output_filename = f'{os_name}_{arch}{output_ext}'
    
    cmd = ['go', 'build', '-o', os.path.join(BINARIES_DIR, output_filename)]
    cmd.extend(['-v', '-x', '-ldflags', '-s -w'])  # Additional compiler flags if needed
    cmd.append(source_file)

    subprocess.run(cmd, check=True)
    
    # Make the compiled binary executable
    if os_name != 'windows':
        binary_path = os.path.join(BINARIES_DIR, output_filename)
        os.chmod(binary_path, 0o755)  # Set executable permissions

def main():
    print(colorama.Fore.LIGHTRED_EX + SMIRNOFF)
    
    source_file = input("Enter the filename of the Go source script: " + colorama.Fore.WHITE)
    
    for platform in ALL_PLATFORMS:
        print(f"{colorama.Fore.YELLOW}[?] Compiling for {platform}...")
        compile_for_platform(platform, source_file)
        print(f"{colorama.Fore.GREEN}Compilation for {platform} complete.")

    print(f"\n\n{colorama.Fore.GREEN}Cross compilation has been complete! See {BINARIES_DIR}/ to view compiled executables!{colorama.Fore.WHITE}")

if __name__ == '__main__':
    main()
