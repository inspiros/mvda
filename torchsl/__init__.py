try:
    matlab_engine = __import__('matlab.engine')
    del matlab_engine
except ModuleNotFoundError:
    print('[Warning] Matlab engine not found. Please install to use matlab\'s python interface, which enables matlab'
          'implementation of EPSolver and LDAX_SwSb algorithm. Of course you need download and install Matlab first.\n'
          '\t\tThe instructions can be found at https://www.mathworks.com/help/matlab/matlab-engine-for-python.html',
          end='\n\n')
