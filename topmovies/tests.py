import unittest
from topmovies import task_handler

class MovieNameExtractionTest(unittest.TestCase):
    """Test function that extracts the movie name from torrent file name"""
    def testYearAfterName(self):
        #Year after name
        self.movieDetailsTest('Star.Trek.2009.DvDRip-', 'Star Trek', 2009)
        self.movieDetailsTest('Star Trek 2009 DvDRip', 'Star Trek', 2009)
        self.movieDetailsTest('Star.Trek (2009) DvDRip-', 'Star Trek', 2009)
        self.movieDetailsTest('Star.Trek [2009] DvDRip-', 'Star Trek', 2009)
        self.movieDetailsTest('District.9.2009.iTALiAN.MD.R5.XviD-SiLENT[UltimaFrontiera]', 'District 9', 2009)
        self.movieDetailsTest('GI Joe The Rise Of Cobra 2009 DvdRip Xvid {1337x}-Noir', 'GI Joe The Rise Of Cobra', 2009)
        self.movieDetailsTest('Final Engagement 2009 FRENCH DVDRIP XVID-BN DIV ', 'Final Engagement', 2009)
    
    def testMovieQuality(self):    
        self.movieDetailsTest('Star Trek DVDRip XviD-iMBT[RLSLOG.IN]', 'Star Trek', None)
        self.movieDetailsTest('The Taking of Pelham 123 R5 LiNE XviD-DEViSE', 'The Taking of Pelham 123', None)
        self.movieDetailsTest('The Ugly Truth DVDSCR XViD-CAMELOT-[tracker BTARENA org]', 'The Ugly Truth', None)
        self.movieDetailsTest('Imagine That BDRip XviD-DASH-[tracker BTARENA org]', 'Imagine That', None)
        self.movieDetailsTest('Surrogates CAM XviD-IMAGiNE', 'Surrogates', None)
        self.movieDetailsTest('Star Trek (DVDRip) XviD-iMBT[RLSLOG.IN]', 'Star Trek', None)
        self.movieDetailsTest('Star Trek DVDRip XviD-iMBT 1080p [RLSLOG.IN]', 'Star Trek', None)
        self.movieDetailsTest('Zombieland TS XVID-IMAGiNE', 'Zombieland', None) 
        self.movieDetailsTest('Inglourious Basterds PPV XViD-IMAGiNE', 'Inglourious Basterds', None) 
        
    def testCaseSensitive(self):
        #Case check
        self.movieDetailsTest('Star Trek dvdrip XviD-iMBT[RLSLOG.IN]', 'Star Trek', None)
        self.movieDetailsTest('Star Trek DVDRIP XviD-iMBT[RLSLOG.IN]', 'Star Trek', None)
        self.movieDetailsTest('Star Trek DvdRip XviD-iMBT[RLSLOG.IN]', 'Star Trek', None)
    
    def testFormatInName(self):
        #Format name
        self.movieDetailsTest('Transformers Revenge of the Fallen 720p BluRay x264-ETHOS-[tracker BTARENA org]', 'Transformers Revenge of the Fallen', None)
        self.movieDetailsTest('Transformers Revenge of the Fallen 1080p BluRay x264-ETHOS-[tracker BTARENA org]', 'Transformers Revenge of the Fallen', None)
    
    def testNoMatch(self):
        #No hit
        self.movieDetailsTest('No Match', None, None)
        
    def testlimitedInName(self):
        self.movieDetailsTest('My One And Only LiMiTED DVDSCR XviD-ARROW avi', 'My One And Only', None)
        self.movieDetailsTest('The Darjeeling Limited (2007) NTSC DVDR [www.ilovetorrents.com]', 'The Darjeeling Limited', 2007)
        
    def movieDetailsTest(self, raw_name, expected_name, expected_year):
        name, year = task_handler.get_movie_details(raw_name)
        self.assertEquals(name, expected_name)
        self.assertEquals(year, expected_year)