//============================================================================
// Name        : embedding_python.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

#include <Python.h>

#define BOOST_FILESYSTEM_VERSION 3
#include <boost/filesystem.hpp>
#include <boost/regex.hpp>

#include "module_loader.hpp"

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
	Py_SetProgramName(argv[0]);
	Py_Initialize();
	PyObject *mainModule = PyImport_AddModule("__main__");
	filesystem::path workingDir = filesystem::path(filesystem::current_path());

	if (filesystem::is_directory(workingDir))
	{
		for (boost::filesystem::directory_iterator itr(workingDir);
				itr != boost::filesystem::directory_iterator(); ++itr)
		{
			run_scipts(*itr, PyModule_GetDict(mainModule));
		}

	}

	Py_Finalize();
	return 0;
}
