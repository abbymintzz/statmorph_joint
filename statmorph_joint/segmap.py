import sep
from photutils import segmentation
from scipy.ndimage import convolve

def get_segmap(image, psf):
    """
    Create a segmentation map from an image using the SEP package.
    This can be tweaked depending on the image properties, etc.

    Also returns a mask to ignore all other detected objects
    """

    image = convolve(image.copy(), psf)
    bkg = sep.Background(image)
    objects, segmap = sep.extract(image - bkg, 10, minarea=5, segmentation_map=True, err=bkg.globalrms, deblend_cont=1e-3, deblend_nthresh=32)
    main_obj = segmap[segmap.shape[0]//2, segmap.shape[1]//2]
    mask = segmap.copy()
    mask[segmap==main_obj]=0
    mask = mask!=0
    segmap[segmap!=main_obj] = 0

    segmap = segmentation.SegmentationImage(segmap)

    return(segmap, mask)
