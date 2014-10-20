/*
 * module_test.cpp
 *
 *  Created on: 20.10.2014
 *      Author: qxh6010
 */


#include <Python.h>

static PyObject *spam_system(PyObject *self)
{
    printf("nagatz\n");
    Py_RETURN_NONE;
}


static PyMethodDef SpamMethods[] = {
    {"system", (PyCFunction)spam_system, METH_NOARGS, NULL},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyObject *init()
{
	PyObject *mainModule = PyImport_AddModule("__main__");
	PyObject *m = Py_InitModule3("testfunc", SpamMethods, "doc");

	Py_INCREF(m);
	PyModule_AddObject( mainModule, "test", m);

	return PyModule_GetDict(mainModule);
}
