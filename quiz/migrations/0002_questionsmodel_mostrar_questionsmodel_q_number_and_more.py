# Generated by Django 4.0.6 on 2022-07-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsmodel',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='questionsmodel',
            name='q_number',
            field=models.BigIntegerField(default=1, unique=True, verbose_name='Questao Nº'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='ans',
            field=models.CharField(max_length=200, null=True, verbose_name='Resposta (Ex: "option1")'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='op1',
            field=models.CharField(max_length=200, null=True, verbose_name='Opção 1'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='op2',
            field=models.CharField(max_length=200, null=True, verbose_name='Opção 2'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='op3',
            field=models.CharField(max_length=200, null=True, verbose_name='Opção 3'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='op4',
            field=models.CharField(max_length=200, null=True, verbose_name='Opção 4'),
        ),
        migrations.AlterField(
            model_name='questionsmodel',
            name='question',
            field=models.CharField(max_length=200, null=True, verbose_name='Pergunta'),
        ),
    ]
