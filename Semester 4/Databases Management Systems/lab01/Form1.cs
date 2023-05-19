using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace lab01_forms
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daEvent;
        SqlDataAdapter daMatch;
        DataSet dset;

        SqlCommandBuilder cmdBuilder;

        string queryEvent;
        string queryMatch;

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            conn = new SqlConnection(getConnectionString());
            queryEvent = "SELECT * FROM Event";
            queryMatch = "SELECT * FROM Match";

            daEvent = new SqlDataAdapter(queryEvent, conn);
            daMatch = new SqlDataAdapter(queryMatch, conn);
            dset = new DataSet();
            daEvent.Fill(dset, "Event");
            daMatch.Fill(dset, "Match");

            cmdBuilder = new SqlCommandBuilder(daMatch);

            dset.Relations.Add("EventMatch",
                dset.Tables["Event"].Columns["Eid"],
                dset.Tables["Match"].Columns["Eid"]);

            this.dataGridView1.DataSource = dset.Tables["Event"];
            this.dataGridView2.DataSource = this.dataGridView1.DataSource;
            this.dataGridView2.DataMember = "EventMatch";

            cmdBuilder.GetUpdateCommand();
        }

        string getConnectionString()
        {
            return "Data Source=DESKTOP-PQP69PQ\\SQLEXPRESS;" + "Initial Catalog=UFC; Integrated Security=true;";
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            daEvent.Update(dset, "Event");
        }
    }
}
