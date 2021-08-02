def xyxy2yolo(coord, img_size):
    """[summary]

    Args:
        coord ([type]): coordinate of bounding box [xmin, ymin, xmax, ymax]
        img_size ([type]): image size from img.shape of cv2
    """
    xmin, ymin, xmax, ymax = coord 
    h, w = ymax-ymin, xmax-xmin
    x, y = xmax - w/2, ymax - h/2

    img_h, img_w = img_size[:2]
    nx, ny, nw, nh = x / img_w, y / img_h, w / img_w, h / img_h

    return nx, ny, nw, nh
