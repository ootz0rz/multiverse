import imp
import os
import sys
import inspect

class Loader(object):

    def __init__(self, base_class, folder):
        self.base_class = base_class
        self.folder = folder

        self.classes = []

        self._load()

    def get_classes(self):
        return [v['class'] for v in self.classes]

    def get_names(self):
        return [v['name'] for v in self.classes]        

    def _load(self):
        self.classes = []
        abs_path = os.path.abspath(self.folder)
        files = os.listdir(abs_path)

        print "\n----------"
        print "Searching:", abs_path

        for f in files:
            if ".py" == f[-3:].lower():
                full_path = os.path.join(abs_path, f)

                module_name = os.path.splitext(f)[0]

                print '\t', "Found module:", module_name
                info = imp.find_module(module_name, [abs_path])
                module = imp.load_module(module_name, *info)

                # check for classes with our base_class
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj):
                        print '\t\t', 'Checking Class:', name, 'w/', self.base_class.__name__

                        # ignore the base class itself
                        if name == self.base_class.__name__:
                            continue

                        is_valid = False
                        for base in inspect.getmro(obj):
                            if base.__name__ == self.base_class.__name__:
                                is_valid = True
                                break
                        
                        if is_valid:
                            self.classes.append({'name': name, 'class': obj})
                            print '\t\t', '->', 'Base Class Match!'
