#!/usr/bin/env python

import imp

if __name__ == "__main__":
    imp.load_source('Module', '../src/Database.py')
    from Module import *
    db = Database()
    
    # Adding Session
    session = db.newSession('schandra', 'hewelhog', '99-01-01 12:12:12', '3.0alpha', 'database tests')

    # Adding Proposal
    prop1 = db.addProposal('TestPropConf', 'TestPropName', session.sessionID, 1, 'objectHost')
    
    # Adding Config
    db.addConfig(session.sessionID, 'ModuleName1', '1', 'paramName1', 'paramValue1', 'Comment1')
    db.addConfig(session.sessionID, 'ModuleName2', '2', 'paramName2', 'paramValue2', 'Comment2')

    # Adding Config_File
    db.addConfigFile('configFile1', '11111111', session.sessionID)
    db.addConfigFile('configFile2', '22222222', session.sessionID)
    
    # Adding Log
    db.addLog('Error', 'There seems to be some problem', session.sessionID)
    db.addLog('Warning', 'There seems to be some warning', session.sessionID)
    
    # Adding TimeHistory
    db.addTimeHistory(session.sessionID, 99, 333.33, 0, 0)
   
    # Adding Proposal_Field
    db.addProposalField(session.sessionID, prop1.propID, 1);
    
    # Adding SeqHistory
    seq1 = db.addSeqHistory(1, 1, 1, 0.4, 1, 1, 1, 1, 1, session.sessionID, prop1.propID)
    
    # Adding ObsHistory
    obs1 = db.addObservation('u', 1, 1.0, 1, 34.0, 32.0, .9,
                             .9, .2, .2, .2, .1, .1,
                             .1, .1, .1, .1, .1, 1, session.sessionID, 1)
    obs2 = db.addObservation('g', 1, 1.0, 1, 34.0, 32.0, .9,
                             .9, .2, .2, .2, .1, .1,
                             .1, .1, .1, .1, .1, 1, session.sessionID, 1)
    obs3 = db.addObservation('r', 1, 1.0, 1, 34.0, 32.0, .9,
                             .9, .2, .2, .2, .1, .1,
                             .1, .1, .1, .1, .1, 1, session.sessionID, 1)
    
    # Adding AstronomicalSky
    db.addAstronomicalSky(.1, .1, .1, .1, .1, .1, .1, .1,
                          .1, .1, .1, .1, .1, obs1.obsHistID)
    db.addAstronomicalSky(.1, .1, .1, .1, .1, .1, .1, .1,
                          .1, .1, .1, .1, .1, obs2.obsHistID)
    db.addAstronomicalSky(.1, .1, .1, .1, .1, .1, .1, .1,
                          .1, .1, .1, .1, .1, obs3.obsHistID)
    
    # Adding Atmosphere
    db.addAtmosphere(.1, .1, .1, obs1.obsHistID)
    db.addAtmosphere(.1, .1, .1, obs2.obsHistID)
    db.addAtmosphere(.1, .1, .1, obs3.obsHistID)
    
    # Adding SeqHistory_ObsHistory
    db.addSeqHistoryObsHistory(seq1.sequenceID, obs1.obsHistID)
    
    # Adding ObsHistory_Proposal
    db.addObsHistoryProposal(prop1.propID, obs1.obsHistID, .9)
    db.addObsHistoryProposal(prop1.propID, obs2.obsHistID, .89)
    db.addObsHistoryProposal(prop1.propID, obs3.obsHistID, .88)

    # Adding SlewHistory
    slew1 = db.addSlewHistory(1, .1, .2, 6.0, 10.0, obs1.obsHistID)
    slew2 = db.addSlewHistory(1, .1, .2, 5.0, 8.0, obs2.obsHistID)
    slew3 = db.addSlewHistory(1, .1, .2, 4.0, 9.0, obs3.obsHistID)
    
    # Adding SlewState
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 0, slew1.slewID);
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 1, slew1.slewID);
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 0, slew2.slewID);
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 1, slew2.slewID);
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 0, slew3.slewID);
    db.addSlewState(.1, .1, .1, 'tracking', .1, .1, .1, .1,
                    .1, .1, .1, .2, 'u', 1, slew3.slewID);
    
    # Adding SlewActivities
    db.addSlewActivities('t', .1, 'notcritical', slew1.slewID)
    db.addSlewActivities('t', .1, 'notcritical', slew2.slewID)
    db.addSlewActivities('t', .1, 'notcritical', slew3.slewID)
    
    # Adding SlewMaxSpeeds
    db.addSlewMaxSpeeds(.1, .1, .1, .1, .1, slew1.slewID)
    db.addSlewMaxSpeeds(.1, .1, .1, .1, .1, slew2.slewID)
    db.addSlewMaxSpeeds(.1, .1, .1, .1, .1, slew3.slewID)
    
    # Deleting the data
    # delete_all_data()
