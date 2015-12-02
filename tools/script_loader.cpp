#include <iostream>
#include <fstream>

#include <Python.h>

#define BOOST_FILESYSTEM_VERSION 3
#include <boost/filesystem.hpp>
#include <boost/regex.hpp>

void run_scipts(const boost::filesystem::path &p, PyObject *m)
{
	boost::regex filePattern("^.+\\.py$");

	if (!boost::filesystem::is_directory(p))
	{
		if (boost::regex_match(p.leaf().string(), filePattern))
		{
			std::ifstream input(p.string().c_str());

			if (input.is_open())
			{
				std::string str((std::istreambuf_iterator<char>(input)),
						std::istreambuf_iterator<char>());

				PyRun_String(str.c_str(), Py_file_input, m, m);
				input.close();
			}
		}
	}
}

int main(int argc, char **argv)
{
	using namespace boost;
	Py_Initialize();
	PyObject *mainModule = PyImport_AddModule("__main__");
	PyObject *mainDict = PyModule_GetDict(mainModule);
	filesystem::path workingDir = filesystem::path(filesystem::current_path());

	if (argc > 1)
	{
		workingDir = filesystem::path(argv[1]);
	}

	if (filesystem::is_directory(workingDir))
	{
		for (filesystem::directory_iterator itr(workingDir);
				itr != filesystem::directory_iterator(); ++itr)
		{
			run_scipts(*itr, mainDict);
		}

	}
	Py_Finalize();
	return 0;
}
