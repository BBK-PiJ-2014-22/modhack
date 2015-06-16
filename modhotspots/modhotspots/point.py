import math

class Point:

    RADIUS = 3959 #Average radius in miles of the earth

    def __init__(self, lat, lon):
        try:
            if (lat > 90  or lat < -90 or
                lon > 180 or lon < -180):
                raise ValueError("Arguments out of range. Lat: -90 to 90 Lon: -180 to 180")
            else:
                self.lat = lat
                self.lon = lon
        except TypeError:
            raise TypeError("Lat and lon must be numbers")

    def __str__(self):
        return str(self.lat)+", "+ str(self.lon)

    def distanceTo(self, point):
        '''Returns the distance in miles from this point to another

        Uses the haversine formula to calculate where:
        a = sin²(Δφ/2) + cos φ1 * cos φ2 * sin²(Δλ/2)
        c = 2 * atan2( √a, √(1−a) )
        d = R * c

        where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
        '''

        try:
            p1_lat = math.radians(self.lat)
            p2_lat = math.radians(point.lat)
            delta_lat = math.radians(self.lat - point.lat)
            delta_lon = math.radians(self.lon - point.lon)

            a = (math.sin((delta_lat/2))**2 +
                (math.cos(p1_lat) * math.cos(p2_lat) *
                 math.sin(delta_lon/2)**2))

            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = Point.RADIUS * c

            return d
        except (AttributeError):
            raise TypeError("Point.distanceTo must be used with type Point")

    def isInRange(self, point, maxDistance):
        '''Returns True if distance between the points is less than maxDistance (in miles)'''
        return self.distanceTo(point) < maxDistance

