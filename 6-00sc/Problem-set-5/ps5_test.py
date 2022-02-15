# 6.00
# Problem Set 5 Test Suite
import unittest
from ps5 import *

score = 0.0
potential_score = 0.0

def add_potential_points(points):
    global potential_score
    potential_score += points
def add_points(points):
    global score
    score += points

class ProblemSet5NewsStory(unittest.TestCase):
    def setUp(self):
        pass
    def testNewsStoryConstructor(self):
        add_potential_points(1)
        story = NewsStory('', '', '', '', '')
        add_points(1)
    def testNewsStoryGetGuid(self):
        add_potential_points(1)
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.get_guid(), 'test guid')
        add_points(1)
    def testNewsStoryGetTitle(self):
        add_potential_points(1)
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.get_title(), 'test title')
        add_points(1)
    def testNewsStoryGetSubject(self):
        add_potential_points(1)
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.get_subject(), 'test subject')
        add_points(1)
    def testNewsStoryGetSummary(self):
        add_potential_points(1)
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.get_summary(), 'test summary')
        add_points(1)
    def testNewsStoryGetLink(self):
        add_potential_points(1)
        story = NewsStory('test guid', 'test title', 'test subject',
                          'test summary', 'test link')
        self.assertEquals(story.get_link(), 'test link')
        add_points(1)

class ProblemSet5(unittest.TestCase):
    def setUp(self):
        class TrueTrigger:
            def evaluate(self, story): return True

        class FalseTrigger:
            def evaluate(self, story): return False

        self.tt = TrueTrigger()
        self.tt2 = TrueTrigger()
        self.ft = FalseTrigger()
        self.ft2 = FalseTrigger()

    def test1TitleTrigger(self):
        add_potential_points(5)
        koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
        pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
        soda      = NewsStory('', 'Soft drinks are great', '', '', '')
        pink      = NewsStory('', "Soft's the new pink!", '', '', '')
        football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
        microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
        nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
        caps      = NewsStory('', 'soft things are soft', '', '', '')

        s1 = TitleTrigger('SOFT')
        s2  = TitleTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "TitleTrigger failed to fire when the word appeared in the title")
            self.assertTrue(trig.evaluate(pillow), "TitleTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "TitleTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "TitleTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "TitleTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "TitleTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "TitleTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "TitleTrigger fired when the word wasn't really present in the title")
        add_points(5)

    def test2SubjectTrigger(self):
        add_potential_points(5)
        koala     = NewsStory('', '', 'Koala bears are soft and cuddly', '', '')
        pillow    = NewsStory('', '', 'I prefer pillows that are soft.', '', '')
        soda      = NewsStory('', '', 'Soft drinks are great', '', '')
        pink      = NewsStory('', '', "Soft's the new pink!", '', '')
        football  = NewsStory('', '', '"Soft!" he exclaimed as he threw the football', '', '')
        microsoft = NewsStory('', '', 'Microsoft announced today that pillows are bad', '', '')
        nothing   = NewsStory('', '', 'Reuters reports something really boring', '', '')
        caps      = NewsStory('', '', 'soft things are soft', '', '')

        s1 = SubjectTrigger('SOFT')
        s2  = SubjectTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "SubjectTrigger failed to fire when the word appeared in the subject")
            self.assertTrue(trig.evaluate(pillow), "SubjectTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "SubjectTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "SubjectTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "SubjectTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "SubjectTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "SubjectTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "SubjectTrigger fired when the word wasn't really present in the subject")
        add_points(5)

    def test3SummaryTrigger(self):
        add_potential_points(5)
        koala     = NewsStory('', '', '', 'Koala bears are soft and cuddly', '')
        pillow    = NewsStory('', '', '', 'I prefer pillows that are soft.', '')
        soda      = NewsStory('', '', '', 'Soft drinks are great', '')
        pink      = NewsStory('', '', '', "Soft's the new pink!", '')
        football  = NewsStory('', '', '', '"Soft!" he exclaimed as he threw the football', '')
        microsoft = NewsStory('', '', '', 'Microsoft announced today that pillows are bad', '')
        nothing   = NewsStory('', '', '', 'Reuters reports something really boring', '')
        caps      = NewsStory('', '', '', 'soft things are soft', '')

        s1 = SummaryTrigger('SOFT')
        s2  = SummaryTrigger('soft')
        for trig in [s1, s2]:
            self.assertTrue(trig.evaluate(koala), "SummaryTrigger failed to fire when the word appeared in the summary.")
            self.assertTrue(trig.evaluate(pillow), "SummaryTrigger failed to fire when the word had punctuation on it")
            self.assertTrue(trig.evaluate(soda), "SummaryTrigger failed to fire when the case was different")
            self.assertTrue(trig.evaluate(pink), "SummaryTrigger failed to fire when the word had an apostrophe on it")
            self.assertTrue(trig.evaluate(football), "SummaryTrigger failed to fire in the presence of lots of punctuation")
            self.assertTrue(trig.evaluate(caps), "SummaryTrigger is case-sensitive and shouldn't be")
            
            self.assertFalse(trig.evaluate(microsoft), "SummaryTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'")
            self.assertFalse(trig.evaluate(nothing), "SummaryTrigger fired when the word wasn't really present in the summary")
        add_points(5)

    def test4NotTrigger(self):
        add_potential_points(5)
        n = NotTrigger(self.tt)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertFalse(n.evaluate(b), "A NOT trigger applied to 'always true' DID NOT return false")

        y = NotTrigger(self.ft)
        self.assertTrue(y.evaluate(b), "A NOT trigger applied to 'always false' DID NOT return true")
        add_points(5)

    def test5AndTrigger(self):
        add_potential_points(5)
        yy = AndTrigger(self.tt, self.tt2)
        yn = AndTrigger(self.tt, self.ft)
        ny = AndTrigger(self.ft, self.tt)
        nn = AndTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertTrue(yy.evaluate(b), "AND of 'always true' and 'always true' should be true")
        self.assertFalse(yn.evaluate(b), "AND of 'always true' and 'always false' should be false")
        self.assertFalse(ny.evaluate(b), "AND of 'always false' and 'always true' should be false")
        self.assertFalse(nn.evaluate(b), "AND of 'always false' and 'always false' should be false")
        add_points(5)

    def test6OrTrigger(self):
        add_potential_points(5)
        yy = OrTrigger(self.tt, self.tt2)
        yn = OrTrigger(self.tt, self.ft)
        ny = OrTrigger(self.ft, self.tt)
        nn = OrTrigger(self.ft, self.ft2)
        b = NewsStory("guid", "title", "subj", "summary", "link")

        self.assertTrue(yy.evaluate(b), "OR of 'always true' and 'always true' should be true")
        self.assertTrue(yn.evaluate(b), "OR of 'always true' and 'always false' should be true")
        self.assertTrue(ny.evaluate(b), "OR of 'always false' and 'always true' should be true")
        self.assertFalse(nn.evaluate(b), "OR of 'always false' and 'always false' should be false")
        add_points(5)

    def test7PhraseTrigger(self):
        add_potential_points(5)
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')


        self.assertTrue(pt.evaluate(a), "PhraseTrigger doesn't find phrase in title")
        self.assertTrue(pt.evaluate(b), "PhraseTrigger doesn't find phrase in subject")
        self.assertTrue(pt.evaluate(c), "PhraseTrigger doesn't find phrase in summary")
    
        for s in [noa, nob, noc]:
            self.assertFalse(pt.evaluate(s), "PhraseTrigger is case-insensitive, and shouldn't be")
        add_points(5)

    def test8FilterStories(self):
        add_potential_points(5)
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')

        triggers = [pt, self.tt, self.ft]
        stories = [a, b, c, noa, nob, noc]
        filtered_stories = filter_stories(stories, triggers)
        for story in stories:
            self.assertTrue(story in filtered_stories)
        filtered_stories = filter_stories(stories, [self.ft])
        self.assertEquals(len(filtered_stories), 0)
        add_points(5)

    def test8FilterStories2(self):
        add_potential_points(5)
        pt = PhraseTrigger("New York City")
        a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
        b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
        c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
        noa = NewsStory('', "something something new york city", '', '', '')
        nob = NewsStory('', '', "something something new york city", '', '')
        noc = NewsStory('', '', '', "something something new york city", '')

        class MatchTrigger(Trigger):
            def __init__(self, story):
                self.story = story
            def evaluate(self, story):
                return story == self.story
        triggers = [MatchTrigger(a), MatchTrigger(nob)]
        stories = [a, b, c, noa, nob, noc]
        filtered_stories = filter_stories(stories, triggers)
        self.assertTrue(a in filtered_stories)
        self.assertTrue(nob in filtered_stories)
        self.assertEquals(2, len(filtered_stories))
        add_points(5)

'''
    def test9UserTriggers(self):
        # Dependency Injection! (the nasty way):
        triggers = \
                'class Trigger(object):\n   def evaluate():\n       return False\nclass WordTrigger(Trigger):\n            def __init__(self, word):\n                self.word = word.lower()\n                print "Injected!"\n            def hash(self):\n                raise NotImplementedError\nclass SubjectTrigger(Trigger):\n    def __init__(self, word):\n        self.word = word.lower()\n        print "Injected Subject!"\n    def hash(self):\n        return "SUBJECT-" + self.word\nclass TitleTrigger(WordTrigger):\n    def hash(self):\n        return "TITLE-" + self.word\nclass SummaryTrigger(WordTrigger):\n    def hash(self):\n        return "SUMMARY-" + self.word\nclass NotTrigger(Trigger):\n    def __init__(self, trigger):\n        self.trigger = trigger\n        print "Injected!"\n    def hash(self):\n        return "NOT-" + self.trigger.hash()\nclass PhraseTrigger(Trigger):\n    def __init__(self, phrase):\n        self.phrase = phrase\n        print "Injected!"\n    def hash(self):\n        return "PHRASE-" + self.phrase\nclass CompositeTrigger(Trigger):\n    def __init__(self, trigger1, trigger2):\n        self.trigger1 = trigger1\n        self.trigger2 = trigger2\nclass AndTrigger(CompositeTrigger):\n    def hash(self):\n        t1_hash = self.trigger1.hash()\n        t2_hash = self.trigger2.hash()\n        if t1_hash > t2_hash:\n            return "AND-" + t1_hash + "-" + t2_hash\n        else:\n            return "AND-" + t2_hash + "-" + t1_hash\nclass OrTrigger(CompositeTrigger):\n    def hash(self):\n        t1_hash = self.trigger1.hash()\n        t2_hash = self.trigger2.hash()\n        if t1_hash > t2_hash:\n            return "OR-" + t1_hash + "-" + t2_hash\n        else:\n            return "OR-" + t2_hash + "-" + t1_hash\n\n\n'
        import compiler
        f = open('ps5.py')

        add_potential_points(5)
        src = ""
        for line in f:
            if line == "if __name__ == '__main__':\n":
                print "found line!"
                break
            src += line
        src += triggers
        print src
        compiled = compiler.compile(src, 'compile-errors', 'exec')
        exec compiled in locals(), globals()
        t1 = SubjectTrigger('sports')
        t2 = SummaryTrigger('Obama')
        t3 = PhraseTrigger('Hillary Clinton')
        t4 = OrTrigger(t2, t3)
        trigger_map = {t1.hash() : False,
                       t4.hash() : False}
        print trigger_map

        trigger_list = readTriggerConfig("triggers.txt")
        for trigger in trigger_list:
            hash = trigger.hash()
            self.assertTrue(hash in trigger_map)
            self.assertFalse(trigger_map[hash])
            trigger_map[hash] = True
        for found in trigger_map.values():
            self.assertTrue(found, "Missing trigger")
        add_points(5)
'''

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ProblemSet5NewsStory))
    suite.addTest(unittest.makeSuite(ProblemSet5))
    #import t2
    #suite.addTest(unittest.makeSuite(t2.ProblemSet5TriggerFile))
    unittest.TextTestRunner(verbosity=2).run(suite)
    #print "t2 score", t2.score
    #print "t2 potential score", t2.potential_score
    #score += t2.score
    #potential_score += t2.potential_score
    #print "Total score: ", float(score) / float(potential_score) * 4.0

