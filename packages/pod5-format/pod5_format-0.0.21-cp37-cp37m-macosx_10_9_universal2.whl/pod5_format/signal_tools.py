"""
Tools for handling pod5 signals
"""

import numpy
import pod5_format.pod5_format_pybind as pod5_bind


def vbz_decompress_signal(
    compressed_signal: numpy.ndarray, sample_count: int
) -> numpy.ndarray:
    """
    Decompress a numpy array of compressed signal data

    Parameters
    ----------
    compressed_signal : numpy.array
        The array of compressed signal data to decompress.
    sample_count : int
        The sample count of the decompressed data.

    Returns
    -------
    A decompressed numpy int16 array
    """
    signal = numpy.empty(sample_count, dtype="i2")

    pod5_bind.decompress_signal(
        compressed_signal,
        signal,
    )
    return signal


def vbz_decompress_signal_into(
    compressed_signal: numpy.ndarray, output_array: numpy.ndarray
) -> numpy.ndarray:
    """
    Decompress a numpy array of compressed signal data

    Parameters
    ----------
    compressed_signal : numpy.array
        The array of compressed signal data to decompress.
    output_array : numpy.array
        The destination location for signal

    Returns
    -------
    A decompressed numpy int16 array
    """

    pod5_bind.decompress_signal(
        compressed_signal,
        output_array,
    )
    return output_array


def vbz_compress_signal(signal: numpy.ndarray) -> numpy.ndarray:
    """
    Compress a numpy array of signal data

    Parameters
    ----------
    signal : numpy.array
        The array of signal data to compress.

    Returns
    -------
    A compressed numpy byte array
    """

    max_signal_size = pod5_bind.vbz_compressed_signal_max_size(len(signal))
    signal_bytes = numpy.zeros(max_signal_size, dtype="u1")

    size = pod5_bind.compress_signal(signal, signal_bytes)

    signal_bytes = numpy.resize(signal_bytes, size)
    return signal_bytes
