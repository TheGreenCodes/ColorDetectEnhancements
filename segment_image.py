import cv2
from colordetect import ColorDetect

# parse the image.
flowers = ColorDetect('./images/flowers.jpg')

monochromatic, gray, segmented, mask = flowers.get_segmented_image(lower_bound=(20,50,50), upper_bound=(40,255,255))

cv2.imshow('Segmented', segmented)
cv2.imshow('monochromatic', monochromatic)
cv2.imshow('mask image', mask)
# cv2.imshow('grey image', gray)
cv2.waitKey(0)

k = cv2.waitKey(0)

if k == 27: # wait for ESC key to exit    
    cv2.destroyAllWindows()
    # wait for 's' key to save and exit    
elif k == ord('s'): 
    cv2.imwrite('Segmented.png',segmented)
    cv2.imwrite('monochromatic.png',monochromatic)
    cv2.imwrite('mask.png',mask)
    cv2.destroyAllWindows()

