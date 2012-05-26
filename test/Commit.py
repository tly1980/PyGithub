import Framework

class Commit( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.commit = self.g.get_user().get_repo( "PyGithub" ).get_branches()[ 0 ].commit
        self.commit.author.login # to force lazy completion

    def testAttributes( self ):
        self.assertEqual( self.commit.author.login, "jacquev6" )
        self.assertEqual( self.commit.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.commit.committer.login, "jacquev6" )
        self.assertEqual( len( self.commit.files ), 1 )
        self.assertEqual( self.commit.files[ 0 ].additions, 0 )
        self.assertEqual( self.commit.files[ 0 ].blob_url, "https://github.com/jacquev6/PyGithub/blob/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( self.commit.files[ 0 ].changes, 20 )
        self.assertEqual( self.commit.files[ 0 ].deletions, 20 )
        self.assertEqual( self.commit.files[ 0 ].filename, "github/GithubObjects/GitAuthor.py" )
        self.assertTrue( isinstance( self.commit.files[ 0 ].patch, ( str, unicode ) ) )
        self.assertEqual( self.commit.files[ 0 ].raw_url, "https://github.com/jacquev6/PyGithub/raw/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( self.commit.files[ 0 ].sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.commit.files[ 0 ].status, "modified" )
        self.assertEqual( len( self.commit.parents ), 1 )
        self.assertEqual( self.commit.parents[ 0 ].sha, "b46ed0dfde5ad02d3b91eb54a41c5ed960710eae" )
        self.assertEqual( self.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.commit.stats.deletions, 20 )
        self.assertEqual( self.commit.stats.additions, 0 )
        self.assertEqual( self.commit.stats.total, 20 )
        self.assertEqual( self.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )

    def testGetComments( self ):
        self.assertListKeyEqual( self.commit.get_comments(), lambda c: c.id, [ 1347033, 1347083, 1347397, 1349654 ] )

    def testCreateComment( self ):
        comment = self.commit.create_comment( "Comment created by PyGithub" )
        self.assertEqual( comment.id, 1361949 )
        self.assertEqual( comment.line, None )
        self.assertEqual( comment.path, None )
        self.assertEqual( comment.position, None )

    def testCreateCommentOnFileLine( self ):
        comment = self.commit.create_comment( "Comment created by PyGithub", path = "codegen/templates/GithubObject.MethodBody.UseResult.py", line = 26 )
        self.assertEqual( comment.id, 1362000 )
        self.assertEqual( comment.line, 26 )
        self.assertEqual( comment.path, "codegen/templates/GithubObject.MethodBody.UseResult.py" )
        self.assertEqual( comment.position, None )

    def testCreateCommentOnFilePosition( self ):
        comment = self.commit.create_comment( "Comment also created by PyGithub", path = "codegen/templates/GithubObject.MethodBody.UseResult.py", position = 3 )
        self.assertEqual( comment.id, 1362001 )
        self.assertEqual( comment.line, None )
        self.assertEqual( comment.path, "codegen/templates/GithubObject.MethodBody.UseResult.py" )
        self.assertEqual( comment.position, 3 )
