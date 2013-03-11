# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bill'
        db.create_table('lawdiff_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('json_archive', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jsonmirror.JSON_Archive'])),
            ('json_details', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('lawdiff', ['Bill'])

        # Adding model 'Bill_File'
        db.create_table('lawdiff_bill_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lawdiff.Bill'])),
            ('converted_bill_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parsed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('lawdiff', ['Bill_File'])


    def backwards(self, orm):
        # Deleting model 'Bill'
        db.delete_table('lawdiff_bill')

        # Deleting model 'Bill_File'
        db.delete_table('lawdiff_bill_file')


    models = {
        'jsonmirror.json_archive': {
            'Meta': {'object_name': 'JSON_Archive'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parsed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jsonmirror.JSON_Archive_Set']"})
        },
        'jsonmirror.json_archive_set': {
            'Meta': {'object_name': 'JSON_Archive_Set'},
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        'lawdiff.bill': {
            'Meta': {'object_name': 'Bill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_archive': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jsonmirror.JSON_Archive']"}),
            'json_details': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'lawdiff.bill_file': {
            'Meta': {'object_name': 'Bill_File'},
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lawdiff.Bill']"}),
            'converted_bill_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parsed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['lawdiff']