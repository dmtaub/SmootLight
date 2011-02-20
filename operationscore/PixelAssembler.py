from operationscore.SmootCoreObject import *
import util.Geo as Geo
import pdb
class PixelAssembler(SmootCoreObject):
    def init(self):
        self.validateArgs('PixelAssembler.params')
        self.initLayout()
    def layoutFunc(self, lastLocation): #Must be defined by inheriting class.
        #Returns tuple pair (x,y)
        pass
    def getPixelLocations(self): #returns a complete list of locations of Pixels
        #for a strip
        locations = [self.argDict['originLocation']]
        for pixelIndex in range(self['numPixels']-1): #-1 because origin
            #already exists
            newLocation = self.layoutFunc(locations[-1]) 
            if newLocation == None:
                raise Exception('Location cannot be null.  layoutFunc not \
                defined or improperly defined.')
            if Geo.dist(newLocation, locations[-1]) > \
                    self['pixelToPixelSpacing']:
                        raise Exception('Illegal pixel location.  Distance \
                        between adjacent pixels must be less than \
                        pixelToPixelSpacing.  Illegal distance is between '+str(pixelIndex) + ' and'\
                                         + str(pixelIndex+1))
            locations.append(newLocation)
        if self['Reverse']:
            locations.reverse()
        return locations
    def initLayout(self):
        pass
    def getStripArgs(self): #TODO: triage and remove
        return self.argDict
