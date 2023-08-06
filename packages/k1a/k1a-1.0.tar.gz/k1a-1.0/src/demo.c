#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *K1Error;

static PyObject *k1a_system(PyObject *self, PyObject *args) {
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command)) return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(K1Error, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}

static PyMethodDef K1aMethods[] = {
    {"system", k1a_system, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef k1amodule = {
    PyModuleDef_HEAD_INIT, "k1a", /* name of module */
    NULL,                         /* module documentation, may be NULL */
    -1, /* size of per-interpreter state of the module,
           or -1 if the module keeps state in global variables. */
    K1aMethods};

PyMODINIT_FUNC PyInit_k1a(void) {
    PyObject *m;

    m = PyModule_Create(&k1amodule);
    if (m == NULL) return NULL;

    K1Error = PyErr_NewException("k1a.error", NULL, NULL);
    Py_XINCREF(K1Error);
    if (PyModule_AddObject(m, "error", K1Error) < 0) {
        Py_XDECREF(K1Error);
        Py_CLEAR(K1Error);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
