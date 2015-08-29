# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_air_modes_swig', [dirname(__file__)])
        except ImportError:
            import _air_modes_swig
            return _air_modes_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_air_modes_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _air_modes_swig = swig_import_helper()
    del swig_import_helper
else:
    import _air_modes_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _air_modes_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _air_modes_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _air_modes_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _air_modes_swig.high_res_timer_epoch()
class preamble(object):
    """Proxy of C++ gr::air_modes::preamble class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def make(channel_rate, threshold_db):
        """make(float channel_rate, float threshold_db) -> preamble_sptr"""
        return _air_modes_swig.preamble_make(channel_rate, threshold_db)

    make = staticmethod(make)

    def set_rate(self, channel_rate):
        """set_rate(preamble self, float channel_rate)"""
        return _air_modes_swig.preamble_set_rate(self, channel_rate)


    def set_threshold(self, threshold_db):
        """set_threshold(preamble self, float threshold_db)"""
        return _air_modes_swig.preamble_set_threshold(self, threshold_db)


    def get_rate(self):
        """get_rate(preamble self) -> float"""
        return _air_modes_swig.preamble_get_rate(self)


    def get_threshold(self):
        """get_threshold(preamble self) -> float"""
        return _air_modes_swig.preamble_get_threshold(self)

    __swig_destroy__ = _air_modes_swig.delete_preamble
    __del__ = lambda self: None
preamble_swigregister = _air_modes_swig.preamble_swigregister
preamble_swigregister(preamble)

def preamble_make(channel_rate, threshold_db):
    """preamble_make(float channel_rate, float threshold_db) -> preamble_sptr"""
    return _air_modes_swig.preamble_make(channel_rate, threshold_db)

class slicer(object):
    """Proxy of C++ gr::air_modes::slicer class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(queue):
        """make(msg_queue_sptr queue) -> slicer_sptr"""
        return _air_modes_swig.slicer_make(queue)

    make = staticmethod(make)
    __swig_destroy__ = _air_modes_swig.delete_slicer
    __del__ = lambda self: None
slicer_swigregister = _air_modes_swig.slicer_swigregister
slicer_swigregister(slicer)

def slicer_make(queue):
    """slicer_make(msg_queue_sptr queue) -> slicer_sptr"""
    return _air_modes_swig.slicer_make(queue)

class preamble_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::air_modes::preamble)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::air_modes::preamble)> self) -> preamble_sptr
        __init__(boost::shared_ptr<(gr::air_modes::preamble)> self, preamble p) -> preamble_sptr
        """
        this = _air_modes_swig.new_preamble_sptr(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __deref__(self):
        """__deref__(preamble_sptr self) -> preamble"""
        return _air_modes_swig.preamble_sptr___deref__(self)

    __swig_destroy__ = _air_modes_swig.delete_preamble_sptr
    __del__ = lambda self: None

    def make(self, channel_rate, threshold_db):
        """make(preamble_sptr self, float channel_rate, float threshold_db) -> preamble_sptr"""
        return _air_modes_swig.preamble_sptr_make(self, channel_rate, threshold_db)


    def set_rate(self, channel_rate):
        """set_rate(preamble_sptr self, float channel_rate)"""
        return _air_modes_swig.preamble_sptr_set_rate(self, channel_rate)


    def set_threshold(self, threshold_db):
        """set_threshold(preamble_sptr self, float threshold_db)"""
        return _air_modes_swig.preamble_sptr_set_threshold(self, threshold_db)


    def get_rate(self):
        """get_rate(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_get_rate(self)


    def get_threshold(self):
        """get_threshold(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_get_threshold(self)


    def history(self):
        """history(preamble_sptr self) -> unsigned int"""
        return _air_modes_swig.preamble_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(preamble_sptr self, int which, int delay)
        declare_sample_delay(preamble_sptr self, unsigned int delay)
        """
        return _air_modes_swig.preamble_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(preamble_sptr self, int which) -> unsigned int"""
        return _air_modes_swig.preamble_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(preamble_sptr self) -> int"""
        return _air_modes_swig.preamble_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(preamble_sptr self) -> double"""
        return _air_modes_swig.preamble_sptr_relative_rate(self)


    def start(self):
        """start(preamble_sptr self) -> bool"""
        return _air_modes_swig.preamble_sptr_start(self)


    def stop(self):
        """stop(preamble_sptr self) -> bool"""
        return _air_modes_swig.preamble_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(preamble_sptr self, unsigned int which_input) -> uint64_t"""
        return _air_modes_swig.preamble_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(preamble_sptr self, unsigned int which_output) -> uint64_t"""
        return _air_modes_swig.preamble_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(preamble_sptr self) -> int"""
        return _air_modes_swig.preamble_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(preamble_sptr self, int m)"""
        return _air_modes_swig.preamble_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(preamble_sptr self)"""
        return _air_modes_swig.preamble_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(preamble_sptr self) -> bool"""
        return _air_modes_swig.preamble_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(preamble_sptr self, int m)"""
        return _air_modes_swig.preamble_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(preamble_sptr self) -> int"""
        return _air_modes_swig.preamble_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(preamble_sptr self, int i) -> long"""
        return _air_modes_swig.preamble_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(preamble_sptr self, long max_output_buffer)
        set_max_output_buffer(preamble_sptr self, int port, long max_output_buffer)
        """
        return _air_modes_swig.preamble_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(preamble_sptr self, int i) -> long"""
        return _air_modes_swig.preamble_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(preamble_sptr self, long min_output_buffer)
        set_min_output_buffer(preamble_sptr self, int port, long min_output_buffer)
        """
        return _air_modes_swig.preamble_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(preamble_sptr self, int which) -> float
        pc_input_buffers_full(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(preamble_sptr self, int which) -> float
        pc_input_buffers_full_avg(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(preamble_sptr self, int which) -> float
        pc_input_buffers_full_var(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(preamble_sptr self, int which) -> float
        pc_output_buffers_full(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(preamble_sptr self, int which) -> float
        pc_output_buffers_full_avg(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(preamble_sptr self, int which) -> float
        pc_output_buffers_full_var(preamble_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.preamble_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(preamble_sptr self) -> float"""
        return _air_modes_swig.preamble_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(preamble_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _air_modes_swig.preamble_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(preamble_sptr self)"""
        return _air_modes_swig.preamble_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(preamble_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _air_modes_swig.preamble_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(preamble_sptr self) -> int"""
        return _air_modes_swig.preamble_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(preamble_sptr self) -> int"""
        return _air_modes_swig.preamble_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(preamble_sptr self, int priority) -> int"""
        return _air_modes_swig.preamble_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(preamble_sptr self) -> std::string"""
        return _air_modes_swig.preamble_sptr_name(self)


    def symbol_name(self):
        """symbol_name(preamble_sptr self) -> std::string"""
        return _air_modes_swig.preamble_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(preamble_sptr self) -> io_signature_sptr"""
        return _air_modes_swig.preamble_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(preamble_sptr self) -> io_signature_sptr"""
        return _air_modes_swig.preamble_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(preamble_sptr self) -> long"""
        return _air_modes_swig.preamble_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(preamble_sptr self) -> basic_block_sptr"""
        return _air_modes_swig.preamble_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(preamble_sptr self, int ninputs, int noutputs) -> bool"""
        return _air_modes_swig.preamble_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(preamble_sptr self) -> std::string"""
        return _air_modes_swig.preamble_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(preamble_sptr self, std::string name)"""
        return _air_modes_swig.preamble_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(preamble_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _air_modes_swig.preamble_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(preamble_sptr self) -> swig_int_ptr"""
        return _air_modes_swig.preamble_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(preamble_sptr self) -> swig_int_ptr"""
        return _air_modes_swig.preamble_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(preamble_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _air_modes_swig.preamble_sptr_message_subscribers(self, which_port)

preamble_sptr_swigregister = _air_modes_swig.preamble_sptr_swigregister
preamble_sptr_swigregister(preamble_sptr)

preamble_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
preamble = preamble.make;

class slicer_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::air_modes::slicer)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::air_modes::slicer)> self) -> slicer_sptr
        __init__(boost::shared_ptr<(gr::air_modes::slicer)> self, slicer p) -> slicer_sptr
        """
        this = _air_modes_swig.new_slicer_sptr(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __deref__(self):
        """__deref__(slicer_sptr self) -> slicer"""
        return _air_modes_swig.slicer_sptr___deref__(self)

    __swig_destroy__ = _air_modes_swig.delete_slicer_sptr
    __del__ = lambda self: None

    def make(self, queue):
        """make(slicer_sptr self, msg_queue_sptr queue) -> slicer_sptr"""
        return _air_modes_swig.slicer_sptr_make(self, queue)


    def history(self):
        """history(slicer_sptr self) -> unsigned int"""
        return _air_modes_swig.slicer_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(slicer_sptr self, int which, int delay)
        declare_sample_delay(slicer_sptr self, unsigned int delay)
        """
        return _air_modes_swig.slicer_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(slicer_sptr self, int which) -> unsigned int"""
        return _air_modes_swig.slicer_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(slicer_sptr self) -> int"""
        return _air_modes_swig.slicer_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(slicer_sptr self) -> double"""
        return _air_modes_swig.slicer_sptr_relative_rate(self)


    def start(self):
        """start(slicer_sptr self) -> bool"""
        return _air_modes_swig.slicer_sptr_start(self)


    def stop(self):
        """stop(slicer_sptr self) -> bool"""
        return _air_modes_swig.slicer_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(slicer_sptr self, unsigned int which_input) -> uint64_t"""
        return _air_modes_swig.slicer_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(slicer_sptr self, unsigned int which_output) -> uint64_t"""
        return _air_modes_swig.slicer_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(slicer_sptr self) -> int"""
        return _air_modes_swig.slicer_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(slicer_sptr self, int m)"""
        return _air_modes_swig.slicer_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(slicer_sptr self)"""
        return _air_modes_swig.slicer_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(slicer_sptr self) -> bool"""
        return _air_modes_swig.slicer_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(slicer_sptr self, int m)"""
        return _air_modes_swig.slicer_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(slicer_sptr self) -> int"""
        return _air_modes_swig.slicer_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(slicer_sptr self, int i) -> long"""
        return _air_modes_swig.slicer_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(slicer_sptr self, long max_output_buffer)
        set_max_output_buffer(slicer_sptr self, int port, long max_output_buffer)
        """
        return _air_modes_swig.slicer_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(slicer_sptr self, int i) -> long"""
        return _air_modes_swig.slicer_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(slicer_sptr self, long min_output_buffer)
        set_min_output_buffer(slicer_sptr self, int port, long min_output_buffer)
        """
        return _air_modes_swig.slicer_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(slicer_sptr self, int which) -> float
        pc_input_buffers_full(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(slicer_sptr self, int which) -> float
        pc_input_buffers_full_avg(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(slicer_sptr self, int which) -> float
        pc_input_buffers_full_var(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(slicer_sptr self, int which) -> float
        pc_output_buffers_full(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(slicer_sptr self, int which) -> float
        pc_output_buffers_full_avg(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(slicer_sptr self, int which) -> float
        pc_output_buffers_full_var(slicer_sptr self) -> pmt_vector_float
        """
        return _air_modes_swig.slicer_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(slicer_sptr self) -> float"""
        return _air_modes_swig.slicer_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(slicer_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _air_modes_swig.slicer_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(slicer_sptr self)"""
        return _air_modes_swig.slicer_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(slicer_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _air_modes_swig.slicer_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(slicer_sptr self) -> int"""
        return _air_modes_swig.slicer_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(slicer_sptr self) -> int"""
        return _air_modes_swig.slicer_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(slicer_sptr self, int priority) -> int"""
        return _air_modes_swig.slicer_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(slicer_sptr self) -> std::string"""
        return _air_modes_swig.slicer_sptr_name(self)


    def symbol_name(self):
        """symbol_name(slicer_sptr self) -> std::string"""
        return _air_modes_swig.slicer_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(slicer_sptr self) -> io_signature_sptr"""
        return _air_modes_swig.slicer_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(slicer_sptr self) -> io_signature_sptr"""
        return _air_modes_swig.slicer_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(slicer_sptr self) -> long"""
        return _air_modes_swig.slicer_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(slicer_sptr self) -> basic_block_sptr"""
        return _air_modes_swig.slicer_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(slicer_sptr self, int ninputs, int noutputs) -> bool"""
        return _air_modes_swig.slicer_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(slicer_sptr self) -> std::string"""
        return _air_modes_swig.slicer_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(slicer_sptr self, std::string name)"""
        return _air_modes_swig.slicer_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(slicer_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _air_modes_swig.slicer_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(slicer_sptr self) -> swig_int_ptr"""
        return _air_modes_swig.slicer_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(slicer_sptr self) -> swig_int_ptr"""
        return _air_modes_swig.slicer_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(slicer_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _air_modes_swig.slicer_sptr_message_subscribers(self, which_port)

slicer_sptr_swigregister = _air_modes_swig.slicer_sptr_swigregister
slicer_sptr_swigregister(slicer_sptr)

slicer_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
slicer = slicer.make;



