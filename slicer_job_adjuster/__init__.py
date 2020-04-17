from girder import events
from girder import plugin


def _onRun(event):
    # Here, you can check event.info and see if this is a job that should be
    # modified.  For instance, if we need an annotation input in xml form, we
    # could fetch the most recent annotation from the input image.  As an
    # example, in the Nuclei Detection example, the input image's *file* (not
    # item) ID is stored in 'inputImageFile'.  We could fetch an annotation,
    # convert it to xml, and save it as a Girder file, then put that file ID
    # in another input parameter so that the worker would download the XML file
    # as part of the job.
    print(event.info)


def _onUpload(event):
    # Here we can check if the upload is from one of our jobs.  If it is, we
    # could, for instance, move and rename the file to desired spot, or
    # convert an output annotation (either from the json file or from the
    # ingested annotation in the database) to an xml file.  See HistomicsUI
    # for an example of processing a file upload.
    print(event.info)


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'Slicer Job Adjuster'

    def load(self, info):
        # load plugins you depend on
        plugin.getPlugin('slicer_cli_web').load(info)

        from slicer_cli_web.models import DockerImageItem

        # We want to bind to the endpoint for each algorithm we care about;
        # the endpoint might have a Girder ID as part of it, so we enumerate
        # the endpoints for this process.
        for image in DockerImageItem.findAllImages():
            for cli in image.getCLIs():
                path = 'slicer_cli_web/cli/%s/run' % cli._id
            events.bind('rest.post.%s.before' % path, 'slicer_job_adjuster', _onRun)
        events.bind('data.process', 'slicer_job_adjuster', _onUpload)
