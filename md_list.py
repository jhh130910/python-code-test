''' module list '''

module_dict = { 'index ': [ 'https://docs.python.org/3.6/index.html','https://docs.python.org/3/py-modindex.html'],
'argparse':'Command-line option and argument parsing.',
'array':'Manage sequences of fixed-type data efficiently.',
'asyncio':'Asynchronous I/O, event loop, and concurrency tools',
'atexit':'Register shutdown callbacks',
'base64':'Encode binary data with ASCII characters.',
'bisect':'Maintains a list in sorted order without having to call sort each time an item is added to the list.',
'bz2':'bzip2 compression',
'calendar':'Classes for working with year, month, and week-oriented values.',
'cgitb':'Mis-named module that provides extended traceback information.',
'cmd':'Create line-oriented command processors.',
'codecs':'String encoding and decoding.',
'collections':'Container data types.',
'collections.abc':'Abstract base classes for container data types.',
'compileall':'Byte-compile Source Files',
'concurrent':' concurrent.futures:Managing Pools of Concurrent Tasks',
'configparser':'Read/write configuration files similar to Windows INI files',
'contextlib':'Utilities for creating and working with context managers.',
'copy':'Duplicating objects.',
'csv':'Read and write comma separated value files.',
'datetime':'Date and time value manipulation.',
'dbm':'Unix Key-Value Databases',
'decimal':'Fixed and floating point math',
'difflib':'Compare sequences, especially lines of text.',
'dis':'Python Bytecode Disassembler',
'doctest':'Write automated tests as part of the documentation for a module.',
'ensurepip':'Install the Python Package Installer, pip',
'enum':'Defines enumeration type',
'filecmp':'Compare files and directories on the file system.',
'fileinput':'Process lines from input streams.',
'fnmatch':'Compare filenames with Unix-style glob patterns.',
'fractions':'Implements a class for working with rational numbers.',
'functools':'Tools for working with functions.',
'gc':'Garbage Collector',
'getopt':'Command line option parsing',
'getpass':'Prompt for a password securely',
'gettext':'Message Catalogs',
'glob':'Use Unix shell rules to find filenames matching a pattern.',
'grp':'Unix Group Database',
'gzip':'Read and write gzip files',
'hashlib':'Cryptographic hashes and message digests',
'heapq':'In-place heap sort algorithm',
'hmac':'Cryptographic signature and verification of messages.',
'http':' http.cookies:Server-side HTTP cookie tools',
'http.server':'Base classes for implementing web servers.',
'imaplib':'IMAP4 client library',
'importlib':'Interface to module import mechanism.',
'inspect':'Inspect live objects',
'io':'Implements file I/O and provides classes for working with buffers using file-like API.',
'ipaddress':'Classes for working with Internet Protocol (IP) addresses.',
'itertools':'Iterator functions for efficient looping',
'json':'JavaScript Object Notation Serializer',
'linecache':'Read text files efficiently',
'locale':'POSIX cultural localization API',
'logging':'Report status, error, and informational messages.',
'mailbox':'Access and manipulate email archives.',
'math':'Mathematical functions',
'mmap':'Memory-map files',
'multiprocessing':'Manage processes like threads.',
'operator':'Functional interface to built-in operators',
'os':'Portable access to operating system specific features.,os.path:Platform-independent manipulation of filenames.',
'pathlib':'Treat filesystem paths as objects.',
'pdb':'Interactive Debugger',
'pickle':'Object serialization',
'pkgutil':'Package utilities',
'platform':'System version information',
'pprint':'Pretty-print data structures',
'profile':'Performance analysis of Python programs.',
'pstats':'Manipulate and analyze profile statistics.',
'pwd':'Unix Password Database',
'pyclbr':'Class browser',
'pydoc':'Online help for modules',
'queue':'Thread-safe FIFO implementation',
'random':'Pseudorandom number generators',
're':'Searching within and changing text using formal patterns.',
'readline':'The GNU readline library',
'resource':'System resource management',
'sched':'Generic event scheduler.',
'select':'Wait for I/O Efficiently',
'selectors':'I/O Multiplexing Abstractions',
'shelve':'Persistent storage of objects',
'shlex':'Lexical analysis of shell-style syntaxes.',
'shutil':'High-level file operations.',
'signal':'Asynchronous system events',
'site':'Site-wide configuration',
'sitecustomize':'Site-specific configuration',
'smtpd':'Includes classes for implementing SMTP servers.',
'smtplib':'Simple mail transfer protocol client.',
'socket':'Network communication',
'socketserver':'Creating network servers.',
'sqlite3':'Embedded relational database',
'statistics':'Statistical Calculations',
'string':'Contains constants and classes for working with text.',
'struct':'Convert between strings and binary data.',
'subprocess':'Spawning additional processes',
'sys':'System-specific configuration',
'sysconfig':'Interpreter Compile-time Configuration',
'tabnanny':'Scan Python source code looking for suspicious indentation.',
'tarfile':'Tar archive access',
'tempfile':'Temporary file system objects',
'textwrap':'Formatting text paragraphs',
'threading':'Manage concurrent operations',
'time':'Clock time',
'timeit':'Time the execution of small bits of Python code.',
'trace':'Follow Program Flow',
'traceback':'Exceptions and stack traces',
'unittest':'Automated testing framework',
'urllib':'urllib.parse:Split URL into components ,urllib.request:Network Resource Access ,urllib.robotparser:Internet spider access control',
'usercustomize':'User-specific configuration',
'uuid':'Universally unique identifiers',
'venv':'Create isolated installation and execution contexts.',
'warnings':'Non-fatal alerts',
'weakref':'Impermanent references to objects',
'webbrowser':'Displays web pages',
'xml':'xml.etree.ElementTree:XML Manipulation API',
'xmlrpc':'xmlrpc.client:Client library for XML-RPC ,xmlrpc.server:Implements an XML-RPC server.',
'zipfile':'ZIP archive access',
'zipimport':'Load Python code from ZIP archives.',
'zlib':'GNU zlib compression library' }

for a,b in module_dict.items():
    print ( 'Key : {0}   \nValue : {1}'.format ( a , b ) )